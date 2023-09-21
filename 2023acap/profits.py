from typing import List
import collections
import datetime
import time
import bisect
class Solution:
    def calculate_max_profit(self,input_data):
        dates, matrix, seg_profit_ratio = set(), [] ,[]
        stock_details = collections.defaultdict(list)
        for i, row in enumerate(input_data):
            symbol, date, price = row.split(',')
            price = float(price)
            date = int(datetime.datetime.strptime(date, "%m/%d/%Y").strftime("%Y%m%d"))
            matrix.append([symbol, date, price])
        for (symbol, date, price) in matrix:
            stock_details[symbol].append([date, price])
        for s in stock_details.keys():
            sorted_date_price = sorted(stock_details[s], key=lambda x: x[0] )
            for i, (date, price) in enumerate(sorted_date_price):
                if i == 0:
                    pre_price = price
                    pre_date = date
                else:
                    scale = price/pre_price
                    if scale > 1:
                        seg_profit_ratio.append([pre_date, date, scale])
                    pre_date = date
                    pre_price = price
        print("seg profit ratio....")
        seg_profit_ratio = sorted(seg_profit_ratio, key= lambda x: (x[0], x[1]))
        for x in seg_profit_ratio:
            print(x)
        date_profit_ratio = collections.defaultdict(int)
        date_profit_ratio[seg_profit_ratio[0][0]] = 1
        date_profit_ratio[seg_profit_ratio[0][1]] = seg_profit_ratio[0][2]
        print("assign date_profit_ratio for ", seg_profit_ratio[0][1], " = ", date_profit_ratio[seg_profit_ratio[0][1]])
        res = date_profit_ratio[seg_profit_ratio[0][1]]
        for i in range(1, len(seg_profit_ratio)):
            # ratio_at_seg_start = max({date_profit_ratio[key] for key in date_profit_ratio if key <= seg_profit_ratio[i][0]}) #replaced
            date_sorted = sorted(date_profit_ratio.keys())
            index = bisect.bisect_right(date_sorted, seg_profit_ratio[i][0])
            ratio_at_seg_start = date_profit_ratio[date_sorted[index - 1]]

            date_profit_ratio[seg_profit_ratio[i][1]] = ratio_at_seg_start * seg_profit_ratio[i][2]
            print("assign date_profit_ratio for " , seg_profit_ratio[i][1] ,  " = " ,  date_profit_ratio[seg_profit_ratio[i][1]] )
            res = max(res, date_profit_ratio[seg_profit_ratio[i][1]])
        print("date profit ratio...")
        for key, value in date_profit_ratio.items():
            print(key, value)

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

start = time.perf_counter()
max_profit = so.calculate_max_profit(input_data)
print("Maximum profit:", max_profit)
max_profit2 = so.calculate_max_profit(input_data2)
print("Maximum profit 2:", max_profit2)
end = time.perf_counter()
ms = (end - start) * 10 ** 3
print(f"Elapsed {ms:.03f} mill secs.")