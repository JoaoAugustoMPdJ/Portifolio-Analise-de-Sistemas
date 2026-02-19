import pandas as pd


def process_clima(df):
    df["data"] = pd.to_datetime(df["data"])

    result = (
        df.groupby("data")[["temperatura", "chuva_mm"]]
        .mean()
        .reset_index()
    )

    # Para gráfico simples, usamos temperatura
    result = result[["data", "temperatura"]]
    result.columns = ["data", "quantidade"]

    return result
