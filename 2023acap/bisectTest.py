import bisect

def get_recent_price(date, price_dict):
    dates = list(price_dict.keys())
    print(dates)
    index = bisect.bisect_right(dates, date)
    print("index", index)
    # Check if the index is out of bounds or if the date is not in the dictionary
    if index == 0:
        return None  # No date is less than the given date
    else:
        return price_dict[dates[index - 1]]  # Return the price for the most recent available date

# Sample price dictionary
price_dict = {
    '20210916': 100,
    '20210911': 110,
    '20210909': 112,
    '20210918': 120,
    '20210914': 123
}

# Example usage
target_date = '20210912'  # The date for which we want to find the most recent price
recent_price = get_recent_price(target_date, price_dict)

if recent_price is not None:
    print(f"The most recent available price for {target_date} is: {recent_price}")
else:
    print(f"No available price for {target_date}.")
