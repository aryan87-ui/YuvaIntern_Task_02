"""
Week 2 - Data Cleaning and Pre-Processing
Dataset: Sample Superstore Sales Dataset
"""

from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "Sample - Superstore.csv"
OUTPUT_FILE = BASE_DIR / "Superstore_cleaned.csv"


if not INPUT_FILE.exists():
    raise FileNotFoundError(
        f"Input dataset not found: {INPUT_FILE}\n"
        "Place 'Sample - Superstore.csv' in the same folder as this script."
    )


# Load dataset
df = pd.read_csv(INPUT_FILE, encoding="latin1")

print("Shape:", df.shape)
print(df.head())
print(df.info())


# Initial quality checks
print("\nMissing values:\n", df.isna().sum())
print("\nDuplicate rows:", df.duplicated().sum())


# Remove exact duplicates defensively
df = df.drop_duplicates().copy()

# Standardize column names
df.columns = df.columns.str.strip()


# Convert dates
for col in ["Order Date", "Ship Date"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")


# Convert numeric fields
numeric_cols = ["Sales", "Quantity", "Discount", "Profit", "Postal Code"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# Standardize text fields
text_cols = df.select_dtypes(include=["object", "string"]).columns
for col in text_cols:
    df[col] = df[col].astype("string").str.strip()


print("\nMissing values after type conversion:\n", df.isna().sum())


# Date consistency
invalid_date_rows = (
    df["Order Date"].notna()
    & df["Ship Date"].notna()
    & (df["Ship Date"] < df["Order Date"])
).sum()

print("\nInvalid date rows:", invalid_date_rows)


# Basic range checks
print(f"Discount range: {df['Discount'].min()} to {df['Discount'].max()}")
print(f"Quantity range: {df['Quantity'].min()} to {df['Quantity'].max()}")
print(f"Sales range: {df['Sales'].min()} to {df['Sales'].max()}")
print(f"Profit range: {df['Profit'].min()} to {df['Profit'].max()}")


# IQR outlier detection
def add_iqr_flag(dataframe, column, flag_name):
    q1 = dataframe[column].quantile(0.25)
    q3 = dataframe[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    flags = dataframe[column].lt(lower_bound) | dataframe[column].gt(upper_bound)

    print(
        f"\n{column}: Q1={q1:.3f}, Q3={q3:.3f}, "
        f"lower={lower_bound:.3f}, upper={upper_bound:.3f}"
    )
    print(f"{column} IQR flags:", int(flags.sum()))

    dataframe[flag_name] = flags.astype(bool)


add_iqr_flag(df, "Sales", "Sales Outlier Flag")
add_iqr_flag(df, "Profit", "Profit Outlier Flag")


# Feature engineering
df["Ship Duration"] = (df["Ship Date"] - df["Order Date"]).dt.days
df["Loss Flag"] = (df["Profit"] < 0).astype("int8")

df["Profit Margin"] = np.where(
    df["Sales"] != 0,
    df["Profit"] / df["Sales"],
    np.nan,
)

df["Order Year"] = df["Order Date"].dt.year.astype("Int64")
df["Order Month"] = df["Order Date"].dt.month.astype("Int64")
df["Order Quarter"] = (
    df["Order Date"].dt.quarter
    .map(lambda x: f"Q{x}" if pd.notna(x) else pd.NA)
    .astype("string")
)
df["Order Month-Year"] = df["Order Date"].dt.strftime("%Y-%m").astype("string")

df["Discount Bucket"] = pd.cut(
    df["Discount"],
    bins=[-np.inf, 0, 0.2, 0.4, np.inf],
    labels=["No Discount", "Low", "Medium", "High"],
    include_lowest=True,
)

df["Sales Tier"] = pd.qcut(
    df["Sales"],
    q=4,
    labels=["Low", "Medium", "High", "Very High"],
    duplicates="drop",
)


# Final validation
print("\nFinal shape:", df.shape)
print("\nFinal dtypes:\n", df.dtypes)
print("\nFinal missing values:\n", df.isna().sum())

assert df["Order Date"].notna().all(), "Order Date contains missing/invalid values."
assert df["Ship Date"].notna().all(), "Ship Date contains missing/invalid values."
assert (df["Ship Date"] >= df["Order Date"]).all(), (
    "Ship Date cannot be earlier than Order Date."
)
assert (df["Sales"] >= 0).all(), "Sales contains negative values."
assert (df["Quantity"] > 0).all(), "Quantity contains non-positive values."
assert df["Discount"].between(0, 1).all(), (
    "Discount contains values outside the expected 0-1 range."
)
assert df.isna().sum().sum() == 0, "Final dataset contains missing values."
assert df.duplicated().sum() == 0, "Final dataset contains duplicate rows."

print("\nAll final validation checks passed.")


# Export
df.to_csv(OUTPUT_FILE, index=False)
print(f"\nSaved analysis-ready dataset to: {OUTPUT_FILE.name}")
