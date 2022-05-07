stocks = {
    'aapl': 157.28,
    'msft': 274.73,
    'goog': 2313.29,
    'amzn': 2295.45,
    'tsla': 865.65,
    'fb': 203.77,
    'nvda': 186.75,
    'wmt': 149.56,
    'xom': 91.69,
    'jpm': 123.72,
}

ticker_input = input('Please enter stock ticker symbol: ')
ticker = ticker_input.lower()

for name in stocks:
    if name == ticker:
        print(name)
        print(stocks[name])
        print(f'Stock: {name.upper()} Price: {stocks[name]}')
        break

else:
    print('Ticker not found')
