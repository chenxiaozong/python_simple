#-*- coding: utf-8 -*-
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
# 绘制世界人口地图
# 导入世界地图包
import pygal.maps.world
wm = pygal.maps.world.World()
wm.title = "Wrold Populations in 2010 by Country"
wm.add("2010",cc_populations)
wm.render_to_file("world_pop.svg")