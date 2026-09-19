# YuvaIntern Task 02 – Data Cleaning and Pre-Processing

## Project Overview

This project focuses on cleaning, validating, transforming, and preprocessing the Sample Superstore dataset using Python and Pandas.

The objective is to prepare reliable and analysis-ready data while documenting data quality issues, missing values, duplicates, inconsistencies, outliers, transformations, and feature engineering decisions.

---

## Dataset

**Dataset:** Sample Superstore Sales Dataset

The dataset contains sales transactions across different categories, regions, customer segments, and products.

The original dataset contains **9,994 records and 21 columns**.

Key variables include:

- Sales
- Quantity
- Discount
- Profit
- Category
- Sub-Category
- Region
- Segment
- Order Date
- Ship Date

---

## Objectives

The main objectives of this project are:

1. Inspect the dataset structure and data types.
2. Identify missing values.
3. Detect duplicate records.
4. Check data consistency.
5. Validate date fields.
6. Detect potential outliers.
7. Handle data quality issues appropriately.
8. Perform data transformations.
9. Create useful analytical features.
10. Prepare the dataset for further analysis and modeling.

---

## Data Cleaning

The following preprocessing steps were performed:

- Missing-value inspection
- Duplicate detection
- Text standardization
- Date conversion
- Numeric type conversion
- Date consistency validation
- Logical range validation
- Outlier detection using the IQR method
- Feature engineering
- Final data validation

---

## Missing Values

The dataset was checked for missing values before and after preprocessing.

The analysis identified **0 missing cells**, so no imputation or deletion based on missing values was required.

The Python workflow still performs missing-value validation after preprocessing.

---

## Duplicate Records

Exact duplicate rows were checked.

The analysis identified **0 exact duplicate rows**.

The cleaning workflow also performs a defensive duplicate-removal step to ensure that duplicate records do not remain in the analysis-ready dataset.

---

## Data Consistency Checks

The preprocessing workflow checks:

- Date conversion
- Order Date and Ship Date consistency
- Numeric data types
- Sales values
- Quantity values
- Discount range
- Profit values
- Text formatting

Invalid date rows were checked and no invalid date records were identified.

---

## Outlier Detection

Potential outliers were identified using the **Interquartile Range (IQR)** method.

For the dataset:

- Sales outlier flags: **1,167**
- Profit outlier flags: **1,881**

These values are treated as **potential outliers**, not automatically as errors.

Outliers were flagged rather than deleted because extreme sales and profit values can represent legitimate business transactions.

---

## Negative Profit

Negative-profit transactions were retained because they represent potentially meaningful business situations such as discounts, returns, or unprofitable sales.

A `Loss Flag` feature was created to identify transactions where:

```text
Profit < 0
```

This allows future analysis of loss-making transactions without deleting potentially important records.

---

## Feature Engineering

The following features were created:

- `Ship Duration`
- `Profit Margin`
- `Loss Flag`
- `Order Year`
- `Order Month`
- `Order Quarter`
- `Order Month-Year`
- `Discount Bucket`
- `Sales Tier`
- `Sales Outlier Flag`
- `Profit Outlier Flag`

After preprocessing, the dataset contains **32 columns**.

---

## Data Transformation

The preprocessing workflow includes:

- Conversion of Order Date and Ship Date to datetime
- Numeric type conversion
- Text standardization
- Date-based feature extraction
- Profit margin calculation
- Discount categorization
- Sales categorization
- Outlier flag creation

For modeling-ready preprocessing, numerical and categorical variables can also be handled using Scikit-learn preprocessing pipelines.

---

## Final Dataset Validation

After preprocessing, the final dataset was validated for:

- Missing values
- Duplicate rows
- Valid dates
- Sales range
- Quantity range
- Discount range
- Profit values
- Data types

The final dataset contains:

```text
Rows: 9,994
Columns: 32
Missing values: 0
Exact duplicates: 0
```

The cleaned dataset is saved as:

```text
Superstore_cleaned.csv
```

---

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- GitHub

---

## Repository Structure

```text
YuvaIntern_Task_02/
│
├── README.md
│
├── report/
│   ├── README.md
│   └── Week_2_Data_Cleaning_and_Preprocessing_Superstore.docx
│
├── code/
│   ├── README.md
│   └── Week_2_Superstore_Cleaning.py
│
├── visualizations/
│   ├── README.md
│   ├── 01_data_quality.png
│   ├── 02_sales_profit_boxplot.png
│   ├── 03_category_sales_profit.png
│   ├── 04_region_sales_profit.png
│   └── 05_outlier_flags.png
│
└── data/
    ├── README.md
    └── Superstore_cleaned.csv
```

---

## How to Run

### 1. Install Python

Make sure Python is installed on your system.

Check the installation:

```bash
python --version
```

### 2. Install Required Libraries

```bash
python -m pip install pandas numpy matplotlib scikit-learn
```

### 3. Place the Dataset

Place the original dataset in the same directory as the Python script:

```text
Sample - Superstore.csv
```

### 4. Run the Python Script

```bash
python Week_2_Superstore_Cleaning.py
```

The script performs data cleaning, validation, transformation, outlier detection, feature engineering, and generates the cleaned dataset.

---

## Report

The detailed **Data Cleaning and Pre-Processing Report** is available in the `report` folder.

The report documents:

- Dataset inspection
- Missing-value analysis
- Duplicate analysis
- Data consistency checks
- Outlier detection
- Cleaning decisions
- Data transformations
- Feature engineering
- Validation
- Reproducibility workflow

---

## Visualizations

The `visualizations` folder contains project charts related to:

- Data quality
- Sales and profit distributions
- Category-level analysis
- Regional analysis
- Outlier detection

---

## Key Results

The preprocessing workflow produced an analysis-ready dataset with:

| Metric | Result |
|---|---:|
| Original rows | 9,994 |
| Original columns | 21 |
| Final columns | 32 |
| Missing cells | 0 |
| Exact duplicate rows | 0 |
| Invalid date rows | 0 |
| Sales outlier flags | 1,167 |
| Profit outlier flags | 1,881 |

---

## Conclusion

This project demonstrates a reproducible data cleaning and preprocessing workflow for the Sample Superstore dataset.

The workflow focuses on data quality validation, transparent preprocessing decisions, outlier analysis, transformation, and feature engineering while preserving important business information.

The resulting `Superstore_cleaned.csv` dataset is ready for further exploratory analysis, visualization, and modeling.

---

## Author

**Aryan Verma**

Data Cleaning and Pre-Processing using Python.
