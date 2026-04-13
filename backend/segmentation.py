import pandas as pd

def customer_segmentation(df):
    df["segment"] = pd.qcut(
        df["OrderCount"],
        q=3,
        labels=["Low Value", "Medium Value", "High Value"]
    )

    return df