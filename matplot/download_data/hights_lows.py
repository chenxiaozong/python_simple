# -*- coding: utf-8 -*-
import csv
# 绘制气温图
from matplotlib import pyplot as plt

# 添加日期
from datetime import datetime


# file_name ='sitka_weather_07-2014.csv' #七月份天气
file_name ='sitka_weather_2014.csv' # sitka整年的天气



dates,highs,lows = [] ,[],[]#存储 日期, 每日最高气温,最低气温

with open (file_name) as fobj:
	reader = csv.reader(fobj)
	header_row = next(reader) #读取reader 中的第一行

	for row  in reader:

		try:
			# 读取日期
			current_date = datetime.strptime(row[0],'%Y-%m-%d')
			#获取最高气温
			high = int(row[1])
			# 读取最低气温
			low = int(row[3])
		except ValueError :
			print(current_date,"missing data")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)



fig = plt.figure(dpi=128,figsize=(10,6))

# 绘制最高气温
plt.plot(dates,highs,c='red')

# 绘制最低气温
plt.plot(dates,lows,c='blue')


# 区域着色
plt.fill_between(dates, highs,lows,facecolor='blue',alpha=0.3)



# 设置图表格式
plt.title("Daily high and low Temperatures - 2014", fontsize=14 )
plt.xlabel('',fontsize=10)
fig.autofmt_xdate()

plt.ylabel("Temperature(F)",fontsize=10)
plt.tick_params(axis='both',which = 'major',labelsize=14)

plt.show()










