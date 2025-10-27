import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("eth_180d.csv", parse_dates=["date"])

# Rolling & Moving Averages
df["ma_7"] = df["price"].rolling(7).mean()
df["ma_30"] = df["price"].rolling(30).mean()

# Rolling volatility (std on 7 days)
df["volatility_7"] = df["price"].rolling(7).std()

# Rolling correlation (price vs volume) on 14 days
df["corr_p_v_14"] = df["price"].rolling(14).corr(df["volume"])

# --- Plots ---
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["price"], label="ETH Price")
plt.plot(df["date"], df["ma_7"], label="MA 7d")
plt.plot(df["date"], df["ma_30"], label="MA 30d")
plt.title("ETH Price with Moving Averages")
plt.xlabel("Date"); plt.ylabel("USD"); plt.legend(); plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df["date"], df["volatility_7"], label="Rolling Volatility (7d)")
plt.title("ETH 7-day Rolling Volatility")
plt.xlabel("Date"); plt.ylabel("Std Dev"); plt.legend(); plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df["date"], df["corr_p_v_14"], label="Rolling Corr(Price, Volume) 14d")
plt.axhline(0, linestyle="--")
plt.title("Rolling Correlation Price vs Volume (14d)")
plt.xlabel("Date"); plt.ylabel("Correlation"); plt.legend(); plt.tight_layout()
plt.show()

# Quick static correlation (whole window)
corr = df["price"].corr(df["volume"])
print(f"Static correlation (price vs volume): {corr:.2f}")
