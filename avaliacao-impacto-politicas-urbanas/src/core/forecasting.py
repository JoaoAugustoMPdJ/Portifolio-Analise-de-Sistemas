import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


class TimeSeriesForecaster:

    def __init__(self, horizon=7):
        self.horizon = horizon
        self.model = LinearRegression()
        self.ready = False

    def fit(self, df):
        if df is None or len(df) < 5:
            return

        df = df.copy()
        df["t"] = (df["data"] - df["data"].min()).dt.days

        X = df[["t"]]
        y = df["valor"]

        self.model.fit(X, y)

        self.last_t = df["t"].max()
        self.last_date = df["data"].max()
        self.ready = True

    def predict(self):
        if not self.ready:
            return None

        future_t = np.arange(
            self.last_t + 1,
            self.last_t + self.horizon + 1
        ).reshape(-1, 1)

        preds = self.model.predict(future_t)

        future_dates = pd.date_range(
            start=self.last_date,
            periods=self.horizon + 1,
            freq="D"
        )[1:]

        return pd.DataFrame({
            "data": future_dates,
            "valor": preds
        })
