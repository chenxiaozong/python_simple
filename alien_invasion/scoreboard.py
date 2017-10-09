# -*- coding: utf-8 -*-
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard( ):
	"""显示计分信息的类"""
	def __init__(self, ai_settings,screen,stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.ai_settings = ai_settings
		self.stats = stats

		# 显示得分信息时使用的字体设置

		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,24)

		# 准备初始得分图像
		self.prep_score()
		self.prep_high_score()#最高得分图像
		self.prep_level() # 显示等级


		# 显示剩余的飞船编组
		self.prep_ships()



	def prep_score(self):
		"""将得分转换为一副渲染的图像"""
		#得分圆整

		round_score = int(round(self.stats.score,-1)) #圆整到10的倍数
		score_str ="score:" + "{:,}".format(round_score)

		self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

		# 将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right -50
		self.score_rect.top = 10


	def prep_high_score(self):
		"""将最高得分转换为一副渲染的图像"""
		#得分圆整

		high_score = int(round(self.stats.high_score,-1)) #圆整到10的倍数
		high_score_str = "high:"+"{:,}".format(high_score)

		self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

		# 将得分放在屏幕顶部重要
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.left = self.score_rect.left

		self.high_score_rect.top = self.score_rect.bottom + 10

	def prep_level(self):
		"""显示等级"""
		level_str = "level:"+str(self.stats.level)

		self.level_image = self.font.render(level_str,True,self.text_color,self.ai_settings.bg_color)
		#将等级放在得分下方

		self.level_rect = self.level_image.get_rect()
		self.level_rect.left = self.score_rect.left
		self.level_rect.top = self.high_score_rect.bottom+10




	def show_score(self):
		"""在屏幕上显示得分面版"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)

		# 绘制飞船
		self.ships.draw(self.screen)


	def prep_ships(self):
		"""显示还剩余多少飞船可用"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10+ship_number*ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
























