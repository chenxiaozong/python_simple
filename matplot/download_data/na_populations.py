# -*- coding: utf-8 -*-
# 北美三个国家的人口数量
# import pygal
# wm = pygal.Worldmap()

# 导入世界地图包
import pygal.maps.world
wm = pygal.maps.world.World()

# 设置标题
wm.title = 'Populations of Countries in North America'

# 添加绘制地区和数据
wm.add("North America ",{'ca':34126000,'us':30934900,'mx':113423000})

# 保存到文件
wm.render_to_file('na_populations.svg')