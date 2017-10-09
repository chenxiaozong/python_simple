# -*- coding: utf-8 -*-

# 随机漫步测试

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个随机漫步实例,并绘制其生成的序列点

# 模拟多次随机漫步- 只要程序处于活动状态,就不断模拟随机漫步

while True:

	rw = RandomWalk(50000)
	rw.fill_walk()
	num_points = rw.num_points

	point_index = list(range(rw.num_points))

	#调整尺寸
	plt.figure(dpi=128,figsize=(10,6)) #指定宽,高,分辨率



	#绘制起点和终点
	plt.scatter(rw.x_values,rw.y_values,c=point_index,cmap=plt.cm.Blues,edgecolors='none', s=1)

	#突出起点和终点
	plt.scatter(0, 0,c='green',edgecolors='none',s=50) #起点
	plt.scatter(rw.x_values[-1], rw.y_values[-1],c='red',edgecolors='none',s=50)

	#隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)



	plt.title("RandomWalk(" + str(num_points)+")")
	plt.show()

	keep_running = input("Make another walk?:(y/n):")
	if keep_running == 'n':
		break





