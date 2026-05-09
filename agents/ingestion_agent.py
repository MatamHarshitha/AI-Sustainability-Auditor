

import pandas as pd


def load_data(path: str) :
   
    return pd.read_csv(path)


def datatypesfix(df: pd.DataFrame) :
   
    
    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df


def fill_missing_values(df: pd.DataFrame) :
  
    
    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna("Unknown")

    return df


def preprocess(df: pd.DataFrame) :
    
    
    df = datatypesfix(df)
    df = fill_missing_values(df)
    
    return df



