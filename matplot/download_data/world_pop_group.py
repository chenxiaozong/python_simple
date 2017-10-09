# -*- coding: utf-8 -*-
# 世界人口

import json

#导入国别码转换模块
from country_codes import get_country_code






# 将数据加载到一个列表中

file_name = "population_data.json"

with open(file_name) as fobj:
	pop_data = json.load(fobj) #读取json数据文件中的数据


# 创建一个包含人口数量的字典
cc_populations ={}





for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':

		country_name = pop_dict['Country Name']
		country_code = pop_dict['Country Code']
		country_pop = int(float(pop_dict['Value']))

		country_code_pygal = get_country_code(country_name) #根据国家名,返回pygal中对应的两位国别码

		if country_code_pygal:
			# print(country_code_pygal +":"+country_name+":" + str(country_pop))
			cc_populations[country_code_pygal] = country_pop  # 将国家代码和人口存入词典
		else:
			print("ERROR -" + country_name)


# 根据人口数量,将国家分为三组 
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}


for cc,pop in cc_populations.items():
	if pop <1000*10000: #小于1000万
		cc_pops_1[cc] = pop
	elif pop <10*10000*10000 : # 1000万到10亿
		cc_pops_2[cc] = pop
	else: #大于10亿
		cc_pops_3[cc] = pop 

print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))
print(cc_pops_3)
# 绘制世界人口地图
# 导入世界地图包
import pygal.maps.world
wm = pygal.maps.world.World()

wm.title = "Wrold Populations in 2010 by Country"

wm.add("0-10m",cc_pops_1)
wm.add("10m-1bn",cc_pops_2)
wm.add(">1bn",cc_pops_3)

wm.render_to_file("world_populations.svg")





















































































