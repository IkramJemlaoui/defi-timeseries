import requests
import pandas as pd

def fetch_eth(days=180):
    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
    params = {"vs_currency": "usd", "days": days}
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    js = r.json()

    prices = pd.DataFrame(js["prices"], columns=["ts", "price"])
    volumes = pd.DataFrame(js["total_volumes"], columns=["ts", "volume"])
    df = prices.merge(volumes, on="ts")
    df["date"] = pd.to_datetime(df["ts"], unit="ms")
    df = df[["date", "price", "volume"]].sort_values("date").reset_index(drop=True)
    return df

if __name__ == "__main__":
    df = fetch_eth(180)
    df.to_csv("eth_180d.csv", index=False)
    print("Saved eth_180d.csv", df.head(), sep="\n")
