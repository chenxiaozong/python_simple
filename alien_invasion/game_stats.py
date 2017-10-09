# -*- coding: utf-8 -*-

class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False	# 游戏是否结束标志

		# 存储最高得分: 任何情况下都不应该重置
		self.high_score = 0

		# 显示等级属性
		self.level = 1
		

	def reset_stats(self):
		"""初始化游戏运行期间可能发生变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit #剩余的可用的飞船
		self.score = 0 # 游戏计分


