
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]


squares = [1,4,9,16,25]

#设置线条粗细
plt.plot(input_values,squares,linewidth=1)

# 设置图表标题,并坐标轴添加标签
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=10)
plt.ylabel("Square of value",fontsize=10)

# 设置刻度标记大小
plt.tick_params(axis='both',labelsize=10)

# 绘制图形
plt.show()


