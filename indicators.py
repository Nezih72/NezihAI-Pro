import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, MACD

def calculate_indicators(df):

    df["RSI"] = RSIIndicator(df["close"], window=14).rsi()

    df["EMA20"] = EMAIndicator(df["close"], window=20).ema_indicator()

    df["EMA50"] = EMAIndicator(df["close"], window=50).ema_indicator()

    macd = MACD(df["close"])

    df["MACD"] = macd.macd()

    df["MACD_SIGNAL"] = macd.macd_signal()

    return df
