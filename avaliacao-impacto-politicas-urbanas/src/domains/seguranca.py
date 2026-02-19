import pandas as pd


def process_seguranca(df, crime_tipo=None, bairro=None):
    df["data"] = pd.to_datetime(df["data"])

    if crime_tipo:
        df = df[df["tipo_crime"].str.lower() == crime_tipo.lower()]

    if bairro:
        df = df[df["bairro"].str.lower() == bairro.lower()]

    if df.empty:
        return None

    result = (
        df.groupby("data")["quantidade"]
        .sum()
        .reset_index()
        .sort_values("data")
    )

    return result
