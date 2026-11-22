stocks = {
    "FB": 10.75,
    "HPQ": 37.2,
    "ACME": 45.23,
    "IBM": 205.55,
    "AAPL": 612.78
}

tech_tickers = ["AAPL", "IBM", "HPQ"]
tech_stocks = {}

for ticker in tech_tickers:
    if ticker in stocks:
        tech_stocks[ticker] = stocks[ticker]

for ticker, price in tech_stocks.items():
    print(f"{ticker} {price}")