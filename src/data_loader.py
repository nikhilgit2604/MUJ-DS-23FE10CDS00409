import pandas as pd


def load_data(path):
    df = pd.read_csv(path)

    df = df.dropna(subset=["text", "category"])

    df["text"] = df["text"].astype(str)
    df["category"] = df["category"].astype(str)

    return df