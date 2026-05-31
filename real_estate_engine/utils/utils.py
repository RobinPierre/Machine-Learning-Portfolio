import pandas as pd
import numpy as np
import hashlib
import json

def compute_md5(df: pd.DataFrame):
    """
    Compute an MD5 checksum for a DataFrame.
    """
    data_bytes = df.to_csv(index=False).encode()
    return hashlib.md5(data_bytes).hexdigest()


def normalize_column(df: pd.DataFrame, column: str):
    """
    Normalize a numeric column to 0–1 range.
    """
    col = df[column]
    min_val = col.min()
    max_val = col.max()
    df[column] = (col - min_val) / (max_val - min_val + 1e-9)
    return df


def load_json(path: str):
    """
    Load a JSON file and return a dict.
    """
    with open(path, "r") as f:
        return json.load(f)


def save_json(path: str, data: dict):
    """
    Save a dict to a JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
