🪙 DeFi Asset Fluctuation Analysis — Ethereum Case Study

 Overview

This project analyzes and forecasts Ethereum (ETH) price fluctuations in the DeFi (Decentralized Finance) ecosystem.
It builds a simple, end-to-end data pipeline — from API collection to time-series forecasting — to understand market behavior and evaluate trends.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![DeFi](https://img.shields.io/badge/Domain-DeFi-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

🎯 Objectives

Collect and structure historical data on Ethereum.

Analyze price trends, volatility, and price–volume correlations.

Predict short-term price movements using Prophet and LSTM models.

Provide clear visual and analytical insights on DeFi asset fluctuations.


⚙️ Pipeline Overview
Step	Script	Description
1. Data Collection	data_fetch.py	Fetches 180 days of ETH price & volume via CoinGecko API → builds the fact table eth_180d.csv.
2. Analysis	analysis.py	Computes moving averages, volatility, and rolling correlations; visualizes trends.
3. Forecasting (Prophet)	prophet_forecast.py	7-day statistical forecast (trend + seasonality).
4. Forecasting (LSTM)	lstm_forecast.py	7-day deep learning forecast based on past 14 days.


📊 Data Structure (Fact Table)
Column	Description
date	Daily timestamp
price	ETH price in USD
volume	Trading volume (USD)
blockchain	Ethereum
asset	ETH
source	CoinGecko


🧠 Tools & Skills

Languages & Libraries: Python, Pandas, Matplotlib, Prophet, TensorFlow/Keras, scikit-learn
Concepts: Time-series analysis, forecasting, data visualization, DeFi analytics
Environment: VS Code, virtual environment (.venv)


🚀 Run the Project
pip install -r requirements.txt
python data_fetch.py       # Collect data
python analysis.py         # Analyze data
python prophet_forecast.py # Prophet forecast
python lstm_forecast.py    # LSTM forecast


📈 Outputs

eth_180d.csv → main fact table

Visualizations (price trends, volatility, correlation)

Forecast charts (Prophet & LSTM predictions)

💬 Summary

A complete mini-project demonstrating data collection, time-series analysis, and predictive modeling on Ethereum —
connecting data science techniques with DeFi market understanding.
