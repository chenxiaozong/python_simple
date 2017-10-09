# -*- coding: utf-8 -*-

import name_function
# from name_function import get_full_name

print("Enter 'q' at any time to quit:")

while True:
	first_name = input("input first name:")
	if first_name == 'q':
		break

	last_name = input("input last name: ")
	if last_name=='q':
		break

	full_name = name_function.get_full_name(first_name,last_name)
	print("Full name is :"+full_name)
	