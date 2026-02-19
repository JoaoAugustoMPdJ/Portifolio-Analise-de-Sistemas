import pandas as pd


def evaluate_impact(df):
    """
    Avalia impacto comparando médias antes e depois do ponto médio da série.
    """

    df = df.sort_values("data")

    split = len(df) // 2

    before = df.iloc[:split]["quantidade"].mean()
    after = df.iloc[split:]["quantidade"].mean()

    impact = after - before

    result = df.copy()
    result["impacto"] = impact

    return result
