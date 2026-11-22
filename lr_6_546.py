stocks = {
    "FB": 10.75,
    "HPQ": 37.2,
    "ACME": 45.23,
    "IBM": 205.55,
    "AAPL": 612.78
}

sorted_stocks = sorted(stocks.items(), key=lambda item: item[1])

for ticker, price in sorted_stocks:
    print(f"{price} {ticker}")