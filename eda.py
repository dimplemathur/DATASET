def data_clean(df, target=None):
    import pandas as pd
    import numpy as np

    df = df.copy()

    for col in df.columns:

        missing_ratio = df[col].isna().mean()
        unique_ratio = df[col].nunique(dropna=True) / len(df)

       
        if missing_ratio > 0.6:
            df.drop(columns=[col], inplace=True)
            continue

        
        if df[col].dtype == object:

            if  unique_ratio > 0.7:
                df[col] = df[col].fillna("unknown")
            else:
                if not df[col].mode().empty:
                    df[col] = df[col].fillna(df[col].mode()[0])

        
        elif np.issubdtype(df[col].dtype, np.number):

            if missing_ratio <= 0.4:
                df[col] = df[col].fillna(df[col].median())
            else:
                df.drop(columns=[col], inplace=True)

        
        elif pd.api.types.is_datetime64_any_dtype(df[col]):

            if missing_ratio <= 0.5:
                df[col] = df[col].fillna("01-01-2025")
            else:
                df.drop(columns=[col], inplace=True)

    return df