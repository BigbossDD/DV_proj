
import pandas as pd
def data_desc(data):
    print("=== DATASET OVERVIEW ===\n")
    
    # Shape
    rows, cols = data.shape
    print(f"Number of rows   : {rows}")
    print(f"Number of columns: {cols}\n")
    
    # Column names
    print("Columns:")
    print(list(data.columns), "\n")
    
    # Data types
    print("=== DATA TYPES ===")
    print(data.dtypes, "\n")
    
    # Basic info (non-null counts)
    print("=== DATA INFO ===")
    data.info()
    print("\n")
    
    # Separate variable types
    numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns
    datetime_cols = data.select_dtypes(include=['datetime64']).columns

    print("=== VARIABLE TYPES SUMMARY ===")
    print(f"Numerical variables ({len(numerical_cols)}):")
    print(list(numerical_cols), "\n")
    
    print(f"Categorical variables ({len(categorical_cols)}):")
    print(list(categorical_cols), "\n")
    
    print(f"Datetime variables ({len(datetime_cols)}):")
    print(list(datetime_cols), "\n")
    
    # Basic stats for numeric columns
    print("=== NUMERICAL SUMMARY ===")
    print(data[numerical_cols].describe(), "\n")
    
    # Unique values for categorical
    print("=== CATEGORICAL SUMMARY (Top 5 values) ===")
    for col in categorical_cols:
        print(f"\n{col}:")
        print(data[col].value_counts().head(5))