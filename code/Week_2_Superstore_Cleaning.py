
# WEEK 2 - DATA CLEANING AND PRE-PROCESSING
# Dataset: Sample - Superstore.csv
# Purpose: inspect, clean, transform, engineer features and export an analysis-ready file.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

RAW_FILE = "Sample - Superstore.csv"
CLEAN_FILE = "Superstore_cleaned.csv"

# 1. Load
df = pd.read_csv(RAW_FILE, encoding="latin1")

# 2. Standardize column labels
df.columns = df.columns.str.strip()

# 3. Basic inspection
print("Shape:", df.shape)
print(df.head())
print(df.info())
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# 4. Remove exact duplicate rows only if they exist.
# In the canonical Week 1 dataset, this count is 0, so no rows are removed.
df = df.drop_duplicates().copy()

# 5. Data types
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

numeric_cols = ["Sales", "Quantity", "Discount", "Profit", "Postal Code"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Postal Code is an identifier, not a continuous business measure.
df["Postal Code"] = df["Postal Code"].astype("Int64")

# 6. Text standardization
text_cols = df.select_dtypes(include="object").columns
for col in text_cols:
    df[col] = df[col].astype("string").str.strip()

# 7. Missing-data validation after conversion
print("\nMissing values after type conversion:\n", df.isna().sum())

# We do NOT impute the canonical dataset because the Week 1 audit found 0 missing cells.
# For a future dataset, use field-specific rules rather than blind mean imputation.

# 8. Logical validation
df["Ship Duration"] = (df["Ship Date"] - df["Order Date"]).dt.days

invalid_dates = df[
    (df["Order Date"].isna()) |
    (df["Ship Date"].isna()) |
    (df["Ship Date"] < df["Order Date"])
]
print("\nInvalid date rows:", len(invalid_dates))

# 9. Range checks
print("\nDiscount range:", df["Discount"].min(), "to", df["Discount"].max())
print("Quantity range:", df["Quantity"].min(), "to", df["Quantity"].max())
print("Sales range:", df["Sales"].min(), "to", df["Sales"].max())
print("Profit range:", df["Profit"].min(), "to", df["Profit"].max())

# 10. IQR outlier detection - FLAG, DO NOT DELETE
def iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return q1, q3, q1 - 1.5 * iqr, q3 + 1.5 * iqr

for col in ["Sales", "Profit"]:
    q1, q3, lower, upper = iqr_bounds(df[col])
    flag_col = f"{col} Outlier Flag"
    df[flag_col] = (df[col] < lower) | (df[col] > upper)
    print(f"\n{col}: Q1={q1:.3f}, Q3={q3:.3f}, lower={lower:.3f}, upper={upper:.3f}")
    print(f"{col} IQR flags:", int(df[flag_col].sum()))

# Negative profit is a business condition, not automatically a data error.
df["Loss Flag"] = (df["Profit"] < 0).astype("int8")

# 11. Feature engineering
df["Profit Margin"] = np.where(
    df["Sales"] != 0, df["Profit"] / df["Sales"], np.nan
)

df["Order Year"] = df["Order Date"].dt.year.astype("Int64")
df["Order Month"] = df["Order Date"].dt.month.astype("Int64")
df["Order Quarter"] = "Q" + df["Order Date"].dt.quarter.astype("string")
df["Order Month-Year"] = df["Order Date"].dt.to_period("M").astype("string")

df["Discount Bucket"] = pd.cut(
    df["Discount"],
    bins=[-0.001, 0, 0.10, 0.20, 0.30, 1.0],
    labels=["No Discount", "0-10%", "10-20%", "20-30%", ">30%"]
)

df["Sales Tier"] = pd.qcut(
    df["Sales"],
    q=4,
    labels=["Low", "Medium", "High", "Very High"],
    duplicates="drop"
)

# 12. Final schema check
print("\nFinal shape:", df.shape)
print("\nFinal dtypes:\n", df.dtypes)
print("\nFinal missing values:\n", df.isna().sum())

# 13. Export
df.to_csv(CLEAN_FILE, index=False)
print(f"\nSaved analysis-ready dataset to: {CLEAN_FILE}")
