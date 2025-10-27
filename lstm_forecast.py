import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load and scale
df = pd.read_csv("eth_180d.csv", parse_dates=["date"])
prices = df[["price"]].values.astype("float32")

scaler = MinMaxScaler()
prices_scaled = scaler.fit_transform(prices)

# Create sequences
def make_sequences(data, lookback=14):
    X, y = [], []
    for i in range(len(data) - lookback):
        X.append(data[i:i+lookback, 0])
        y.append(data[i+lookback, 0])
    X = np.array(X); y = np.array(y)
    return X.reshape((X.shape[0], X.shape[1], 1)), y

lookback = 14
X, y = make_sequences(prices_scaled, lookback)

# Train/test split
split = int(len(X)*0.8)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Model (tiny)
model = Sequential([
    LSTM(32, input_shape=(lookback,1)),
    Dense(1)
])
model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=20, batch_size=16, verbose=0)

# Predict next step iteratively for horizon=7
preds_scaled = []
last_seq = X_test[-1]  # last known window
cur = last_seq.copy()
for _ in range(7):
    p = model.predict(cur[np.newaxis, ...], verbose=0)[0,0]
    preds_scaled.append(p)
    cur = np.concatenate([cur[1:], np.array([[p]])], axis=0)

preds = scaler.inverse_transform(np.array(preds_scaled).reshape(-1,1)).ravel()
print("Next 7-day LSTM preds (approx):", preds)
