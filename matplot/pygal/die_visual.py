# -*- coding: utf-8 -*-

# 测试掷骰子

from die import Die

#同时掷两个骰子,统计两个骰子的点数的和:面数分别为D6 D10
die_1 = Die()
die_2 = Die(10)



results = []
for roll_number in range(1000):
	res = die_1.roll() + die_2.roll()

	results.append(res)

# 分析结果

max_result = die_1.num_sides + die_2.num_sides

frequencies = []
for value  in range(2,max_result+1):
	freq = results.count(value)
	frequencies.append(freq)



print(frequencies)

# 绘制直方图
import pygal

hist = pygal.Bar()

hist.title = "Result of rolling on two D6 1000 times ."

hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']

hist.x_title = "Result"

hist.y_title = "Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('die_visul.svg')



























































