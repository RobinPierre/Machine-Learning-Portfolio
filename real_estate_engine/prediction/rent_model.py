import pandas as pd
from sklearn.linear_model import LinearRegression

def train_rent_model(df: pd.DataFrame, target: str, features: list[str]):
    """
    Train a simple linear regression model for rent prediction.
    Returns the fitted model.
    """
    X = df[features]
    y = df[target]
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_rent(model, df: pd.DataFrame, features: list[str]):
    """
    Generate rent predictions using the trained model.
    """
    return model.predict(df[features])
