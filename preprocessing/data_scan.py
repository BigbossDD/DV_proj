import pandas as pd
import numpy as np

def data_quality_scan(df):

    report = []

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # =========================
    # NUMERICAL ANALYSIS
    # =========================
    for col in numeric_cols:

        series = df[col].dropna()

        # negative values
        negative_count = (series < 0).sum()

        # IQR for outliers
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = ((series < lower_bound) | (series > upper_bound)).sum()

        report.append({
            'column': col,
            'type': 'numeric',
            'count': len(series),
            'missing': df[col].isnull().sum(),
            'negative_values': int(negative_count),
            'outliers_IQR': int(outliers),
            'min': float(series.min()),
            'max': float(series.max()),
            'mean': float(series.mean())
        })

    # =========================
    # CATEGORICAL ANALYSIS
    # =========================
    for col in categorical_cols:

        series = df[col].dropna()

        report.append({
            'column': col,
            'type': 'categorical',
            'count': len(series),
            'missing': df[col].isnull().sum(),
            'unique_values': series.nunique(),
            'top_value': series.mode()[0] if not series.empty else None,
            'top_freq': series.value_counts().iloc[0] if not series.empty else None
        })

    report_df = pd.DataFrame(report)

    print("\n=== DATA QUALITY SUMMARY ===")
    print(report_df)

    return report_df