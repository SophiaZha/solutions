import collections
import datetime

class Solution:
    def calculate_max_profit(self,input_data):
        stocks = set()
        dates = []
        max_profit = 0
        matrix = []
        stock_details = collections.defaultdict(list)
        date_price_ratio = []

        for i, row in enumerate(input_data):
            symbol, date, price = row.split(',')
            stocks.add(symbol)
            price = float(price)
            date = int(datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y%m%d"))
            matrix.append([symbol, date, price])
            print(matrix[i])
        print("-----------------------")
        matrix = sorted(matrix, key=lambda x: (x[1], x[0]))
        for (symbol, date, price) in matrix:
            if date not in dates:
                dates.append(date)
            stock_details[symbol].append([date, price])
        for s in stocks:
            for i, (date, price) in enumerate(stock_details[s]):
                if i == 0:
                    pre_price = price
                    pre_date = date
                else:
                    scale = price/pre_price
                    if scale > 1:
                        date_price_ratio.append([pre_date, date, scale])
                    pre_date = date
                    pre_price = price
        print(" date price ratio....")
        date_price_ratio = sorted(date_price_ratio, key= lambda x: ( x[0], x[1] ))
        for x in date_price_ratio:
            print(x)
        date_end_scale = collections.defaultdict(int)
        date_end_scale[date_price_ratio[0][0]] = 1
        date_end_scale[date_price_ratio[0][1]] = date_price_ratio[0][2]
        res = date_end_scale[date_price_ratio[0][1]]
        for i in range(1, len(date_price_ratio) ):
            curr_max_ratio_at_segment_start = max({date_end_scale[key] for key in date_end_scale if key <= date_price_ratio[i][0]})
            # subset_values = {date_end_scale[key] for key in date_end_scale if key <= 20221522}
            # curr_max_ratio_at_segment_start = max({date_end_scale[key] for key in date_end_scale if key <= 20221522 })
            date_end_scale[date_price_ratio[i][1]] = curr_max_ratio_at_segment_start * date_price_ratio[i][2]
            res = max(res, date_end_scale[date_price_ratio[i][1]] )
        return round(1000.0 * (res -1 ))

so = Solution()
# Sample input data
input_data = ["G,12/19/2022,10","G,12/01/2022,15", "G,12/07/2022,30",
              "I,12/18/2022,240", "I,12/01/2022,100", "I,12/03/2022,120",
              "A,12/01/2022,100", "A,12/04/2022,80", "A,12/20/2022,160", "A,12/21/2022,320"]

input_data = ["C,10/18/2024,41.89","A,10/10/2024, 113.67",
              "A,10/18/2024,120.5", "C,10/10/2024, 43.12"]

input_data2 = ["G,12/19/2023,112.19","G,12/01/2023,116.41", "G,12/07/2023,111.36",
              "I,12/18/2023,134.07", "I,12/01/2023,132.05", "I,12/03/2023,135.19",
              "A,12/01/2023,187.19", "A,12/04/2023,164.33", "A,12/20/2023,180.94", "A,12/21/2023,179.65"]

# Calculate max profit
max_profit = so.calculate_max_profit(input_data)
print("Maximum profit:", max_profit)
max_profit2 = so.calculate_max_profit(input_data2)
print("Maximum profit 2:", max_profit2)
