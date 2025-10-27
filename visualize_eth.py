import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("eth_180d.csv")

plt.plot(df["date"], df["price"], label="Price (USD)")
plt.title("Ethereum Price over 180 days")
plt.xlabel("Date")
plt.ylabel("USD")
plt.legend()
plt.show()
