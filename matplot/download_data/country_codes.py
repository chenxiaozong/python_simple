# -*- coding: utf-8 -*-


from  pygal.maps.world import COUNTRIES

# 定义一个函数,在COUNTRIES中查找并返回国别码

def get_country_code(country_name):
	"""根据指定的国家,返回Pygal使用的两位的国别码"""
	for code ,name in COUNTRIES.items():
		if name ==country_name:
			return code
	# 如果没有找到,返回None
	return None


# # 测试

# china_code = get_country_code("China")
# print(china_code)
