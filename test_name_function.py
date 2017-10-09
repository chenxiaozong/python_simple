# -*- coding: utf-8 -*-

import unittest

from name_function import get_full_name

class  NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""
	def test_first_last_name(self):
		""" 能够正确处理像 Janis Joplin 这样的名字吗? """
		full_name = get_full_name('janis', 'joplin')
		self.assertEqual(full_name,'Janis Jplin')

unittest.main()		