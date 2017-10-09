# -*- coding: utf-8 -*-
# 提取pygal中的国别码- 获取两个字母的  国别码-国家名

# from pygal.i18n import COUNTRIES  已经不存在 ,使用 pygal-maps-world

from  pygal.maps.world import COUNTRIES

# 
for  country_code in sorted(COUNTRIES.keys()):
	print(country_code ,COUNTRIES[country_code])
