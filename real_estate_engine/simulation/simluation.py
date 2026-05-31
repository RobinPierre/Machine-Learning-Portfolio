import numpy as np
import pandas as pd

def monte_carlo(
    base_value: float,
    std_dev: float,
    iterations: int = 1000
):
    """
    Run a simple Monte Carlo simulation around a base value.
    Returns an array of simulated outcomes.
    """
    noise = np.random.normal(loc=0, scale=std_dev, size=iterations)
    return base_value + noise


def scenario_noise(
    df: pd.DataFrame,
    columns: list[str],
    noise_std: float = 0.05
):
    """
    Apply multiplicative noise to selected columns in a DataFrame.
    Example: 5% noise -> value * (1 + epsilon)
    """
    df = df.copy()
    for col in columns:
        eps = np.random.normal(loc=0, scale=noise_std, size=len(df))
        df[col] = df[col] * (1 + eps)
    return df


def simulate_property(
    rent_pred: float,
    price_pred: float,
    vacancy_pred: float,
    appreciation_pred: float,
    iterations: int = 1000
):
    """
    Run Monte Carlo simulations for each prediction component.
    Returns a dict of arrays.
    """
    return {
        "rent": monte_carlo(rent_pred, std_dev=rent_pred * 0.05, iterations=iterations),
        "price": monte_carlo(price_pred, std_dev=price_pred * 0.03, iterations=iterations),
        "vacancy": monte_carlo(vacancy_pred, std_dev=vacancy_pred * 0.10, iterations=iterations),
        "appreciation": monte_carlo(appreciation_pred, std_dev=abs(appreciation_pred) * 0.15, iterations=iterations),
    }
