# YuvaIntern_Task_02
Week 2 Data Cleaning and Pre-Processing project using Python and Pandas on the Sample Superstore dataset.


# YuvaIntern Task 02 – Data Cleaning and Pre-Processing

## Project Overview

This project focuses on cleaning, validating, transforming, and preprocessing the Sample Superstore dataset using Python and Pandas.

The objective is to prepare reliable and analysis-ready data while documenting data quality issues, missing values, duplicates, inconsistencies, outliers, transformations, and feature engineering decisions.

---

## Dataset

**Dataset:** Sample Superstore Sales Dataset

The dataset contains sales transactions across different categories, regions, customer segments, and products.

Key variables include:

- Sales
- Quantity
- Discount
- Profit
- Category
- Sub-Category
- Region
- Customer Segment
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

---

## Missing Values

The Week 1 dataset inspection identified no missing cells.

Therefore, no imputation or deletion based on missing values was required.

The Python workflow still performs missing-value validation after preprocessing.

---

## Duplicate Records

Exact duplicate rows were checked.

No exact duplicate records were identified in the Week 1 analysis.

The cleaning workflow also performs a defensive duplicate-removal step.

---

## Outlier Detection

Potential outliers were identified using the Interquartile Range (IQR) method.

Outliers were flagged rather than automatically deleted because extreme sales and profit values can represent legitimate business transactions.

---

## Feature Engineering

The following features were created:

- Ship Duration
- Profit Margin
- Loss Flag
- Order Year
- Order Month
- Order Quarter
- Order Month-Year
- Discount Bucket
- Sales Tier
- Sales Outlier Flag
- Profit Outlier Flag

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
│   └── Week_2_Data_Cleaning_and_Preprocessing_Superstore.docx
│
├── code/
│   └── Week_2_Superstore_Cleaning.py
│
├── visualizations/
│   ├── 01_data_quality.png
│   ├── 02_sales_profit_boxplot.png
│   ├── 03_category_sales_profit.png
│   ├── 04_region_sales_profit.png
│   └── 05_outlier_flags.png
│
└── data/
    └── Superstore_cleaned.csv
