import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

df = pd.read_csv("eth_180d.csv", parse_dates=["date"])
df_p = df.rename(columns={"date": "ds", "price": "y"})[["ds", "y"]]

m = Prophet(daily_seasonality=True)
m.fit(df_p)

future = m.make_future_dataframe(periods=7)  # next 7 days
fcst = m.predict(future)

fig1 = m.plot(fcst)
plt.title("ETH Price Forecast (Prophet) - Next 7 Days")
plt.show()

# Components (trend/seasonality)
fig2 = m.plot_components(fcst)
plt.show()

# Save key outputs
fcst[["ds","yhat","yhat_lower","yhat_upper"]].tail(10).to_csv("prophet_output.csv", index=False)
print("Saved prophet_output.csv (last rows):")
print(fcst[["ds","yhat","yhat_lower","yhat_upper"]].tail(10))
