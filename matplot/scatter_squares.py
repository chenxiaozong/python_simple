# -*- coding: utf-8 -*-
# 绘制散点图
import matplotlib.pyplot as plt

x_values = list(range(1,101))
y_values =[x**2 for x in x_values]

# plt.scatter(x_values, y_values,c='red',edgecolor='none',s=20) # s=100 设置点的大小
# plt.scatter(x_values, y_values,c=(1,0,0),edgecolor='none',s=20) # s=100 设置点的大小
plt.scatter(x_values, y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=20) # s=100 设置点的大小


# 设置标题,并添加标签
plt.title("Square Numbers",fontsize=14)
plt.xlabel("Value",fontsize=10)
plt.ylabel("Square of values",fontsize=10)

# 设置可读标记大小
plt.tick_params(axis='both',which='major',labelsize=10)

# 保存图像
fig_name = 'squares_plot.png'
plt.savefig(fig_name,bbox_inches='tight') # 文件名:  bbox_inches: 将图标多余的空白区域剪切掉

plt.show()

