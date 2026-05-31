import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def train_appreciation_model(series: pd.Series, lag: int = 6):
    """
    Train a simple autoregressive model for appreciation forecasting.
    series: a pandas Series indexed in time order.
    lag: number of past values to use.
    """
    values = series.values
    X, y = [], []

    for i in range(lag, len(values)):
        X.append(values[i-lag:i])
        y.append(values[i])

    X = np.array(X)
    y = np.array(y)

    model = LinearRegression()
    model.fit(X, y)
    return model

def forecast_appreciation(model, series: pd.Series, steps: int = 1, lag: int = 6):
    """
    Forecast future appreciation values using the trained model.
    """
    history = list(series.values)

    for _ in range(steps):
        x = np.array(history[-lag:]).reshape(1, -1)
        next_val = model.predict(x)[0]
        history.append(next_val)

    return history[-steps:]
