import pandas as pd
import numpy as np

def compute_score(
    rent_pred: float,
    price_pred: float,
    vacancy_pred: float,
    appreciation_pred: float,
    weights: dict[str, float] = None
):
    """
    Compute a composite property score using weighted components.
    """
    if weights is None:
        weights = {
            "rent": 0.35,
            "price": 0.25,
            "vacancy": 0.20,
            "appreciation": 0.20,
        }

    components = {
        "rent": rent_pred,
        "price": -price_pred,          # lower price = better
        "vacancy": -vacancy_pred,      # lower vacancy = better
        "appreciation": appreciation_pred,
    }

    score = sum(components[k] * weights[k] for k in weights)
    return score


def score_dataframe(df: pd.DataFrame, weights: dict[str, float] = None):
    """
    Compute scores for an entire DataFrame with prediction columns:
    - rent_pred
    - price_pred
    - vacancy_pred
    - appreciation_pred
    """
    scores = []
    for _, row in df.iterrows():
        s = compute_score(
            rent_pred=row["rent_pred"],
            price_pred=row["price_pred"],
            vacancy_pred=row["vacancy_pred"],
            appreciation_pred=row["appreciation_pred"],
            weights=weights,
        )
        scores.append(s)

    df["score"] = scores
    return df
