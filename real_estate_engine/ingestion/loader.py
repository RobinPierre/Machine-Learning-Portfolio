import pandas as pd
import hashlib

def load_csv(path: str):
    """
    Load a CSV file and return:
    - dataframe
    - checksum (md5)
    """
    df = pd.read_csv(path)
    checksum = hashlib.md5(df.to_csv(index=False).encode()).hexdigest()
    return df, checksum
