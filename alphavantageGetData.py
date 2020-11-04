import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import selinumScraping
import matplotlib.pyplot as plt

api_key = 'E6PKO5CSPLN5B08A'
symbols = selinumScraping.symbols_list
print('currently most active stocks: ', symbols[0], symbols[1], symbols[2], symbols[3])

my_symbol = None
while my_symbol is None:
    print('enter stock symbol:')
    my_symbol = input()


ts= TimeSeries(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_intraday(symbol=my_symbol, interval='60min', outputsize='full')

period = 60

ti = TechIndicators(key=api_key, output_format='pandas')
data_ti, meta_data_ti = ti.get_sma(symbol=my_symbol, interval='60min', time_period=peroid, series_type='close')

df1 = data_ti
df2 = data_ts['4. close'].iloc[peroid-1::]


df2.index = df1.index
total_df = pd.concat([df1, df2], axis=1)

print(data_ts)

print(total_df.describe())
total_df.plot()
plt.show()


percent = None
while percent != 'exit':
    print('enter the diff% of SMA-CLOSE:', end=' ')
    count = 0
    percent = input()
    for i in total_df.index:
        if (total_df['SMA'].loc[i] - total_df['4. close'].loc[i]) / total_df['SMA'].loc[i] > float(percent):
            count = count + 1
            print('DATE:', i, "SMA:", total_df['SMA'].loc[i], " CLOSE:", total_df['4. close'].loc[i])
    print("count index:", count)
    print('enter exit to leave or press enter to continue:')
    percent = input()
