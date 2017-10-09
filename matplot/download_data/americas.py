# -*- coding: utf-8 -*-
# 突出北美,中美,南美的地图

import pygal.maps.world


wm = pygal.maps.world.World()

wm.add('North America',['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])

wm.render_to_file('americas.svg')