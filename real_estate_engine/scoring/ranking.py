import pandas as pd

def rank_properties(df: pd.DataFrame, score_column: str = "score", ascending: bool = False):
    """
    Rank properties based on a score column.
    ascending=False means highest score gets rank 1.
    """
    df = df.copy()
    df["rank"] = df[score_column].rank(method="dense", ascending=ascending).astype(int)
    df = df.sort_values("rank")
    return df


def top_n(df: pd.DataFrame, n: int, score_column: str = "score"):
    """
    Return the top N properties by score.
    """
    ranked = rank_properties(df, score_column=score_column)
    return ranked.head(n)
