import pandas as pd


def process_mobilidade(df):
    df["data"] = pd.to_datetime(df["data"])

    result = (
        df.groupby(df["data"].dt.date)["fluxo_veiculos"]
        .mean()
        .reset_index()
    )

    result["data"] = pd.to_datetime(result["data"])
    return result
