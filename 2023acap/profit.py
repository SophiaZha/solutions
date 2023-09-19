from collections import defaultdict

def calculate_max_profit(input_data):
    max_profit = 0
    stock_data = defaultdict(float)

    for row in input_data:
        symbol, date, price = row.split(',')
        price = float(price)
        if symbol in stock_data:
            max_profit = max(max_profit, price - stock_data[symbol])
        else:
            stock_data[symbol] = price
    return round(max_profit)

# Sample input data
input_rows = ["IBM,10/24/2022,103", "AAPL,10/24/2022,150", "IBM,10/25/2022,110", "AAPL,10/25/2022,160"]

# Parse input rows and calculate max profit
max_profit = calculate_max_profit(input_rows)
print("Maximum profit:", max_profit)·
