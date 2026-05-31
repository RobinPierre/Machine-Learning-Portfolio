import pandas as pd
from sklearn.linear_model import LinearRegression

def train_price_model(df: pd.DataFrame, target: str, features: list[str]):
    model = LinearRegression()
    model.fit(df[features], df[target])
    return model

def predict_price(model, df: pd.DataFrame, features: list[str]):
    return model.predict(df[features])
