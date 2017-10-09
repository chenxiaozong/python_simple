# 我们创建一个空的Pygame窗口

import pygame

 #导入设置类
from settings import Settings


 #导入飞船类
from ship import Ship


# 导入事件模块
import game_functions as gf


# 导入编组,管理子弹

from pygame.sprite import Group


# 导入外星人
from alien import Alien


# 导入游戏状态模块
from game_stats import GameStats


# 导入button
from button import Button


# 导入计分牌
from scoreboard import Scoreboard


def run_game():
	"""初始化游戏,并创建一个屏幕对象"""
	pygame.init()

	ai_settings = Settings()##实例化设置类

	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

	#创建一艘飞船
	ship = Ship(ai_settings,screen)

	# 创建一个外星人的实例
	alien = Alien(ai_settings, screen)


	#将子弹添加到数组中
	bullets = Group()

	#创建编组,存放多个外星人
	aliens = Group()

	# 创建外星人群
	# gf.create_fleet(ai_settings,screen,aliens)

	gf.create_fleet(ai_settings, screen, ship, aliens)

	#设置标题
	pygame.display.set_caption(ai_settings.title)

	# 创建play按钮
	play_button = Button(ai_settings, screen, "Play")

	# 创建一个用于存储游戏状态的统计信息实例
	stats = GameStats(ai_settings)

	gf.read_game_score(stats)

	#创建一个记分牌
	sb = Scoreboard(ai_settings, screen, stats)

	
	# 开始游戏主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb)


		if stats.game_active:

			ship.update()

			#提取update_bullets() - 更新子弹位置时检查碰撞
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)

			# 外星人移动
			gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
		#更新屏幕
		gf.update_screen(ai_settings, screen, stats,sb,ship,aliens,bullets,play_button)

run_game()












