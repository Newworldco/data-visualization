import csv
from matplotlib import pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[3]))

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形格式
plt.title('每日最高/低气温-2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("华氏摄氏度", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()