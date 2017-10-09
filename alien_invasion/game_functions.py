# -*- coding: utf-8 -*-

# 监测事件的模块

import sys

import pygame


from bullet import Bullet

from alien import Alien

from time import sleep

from button import Button

from scoreboard import Scoreboard

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb):
	"""响应键盘和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_game_score(stats)#保存游戏记录
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings,screen,ship,bullets,stats)  # 按键按下

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ai_settings,screen,ship,bullets)

		elif event.type == pygame.MOUSEBUTTONDOWN:#检查鼠标按下时是否点击play按钮	
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
	"""玩家单机Play按钮时,开始新的游戏"""
	button_clicked =  play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active: #只有非active 状态下点击按钮才有效
		# 隐藏光标
		pygame.mouse.set_visible(False)


		# 重置游戏设置 
		ai_settings.initialize_dynamic_settings()

		# 重置游戏
		stats.reset_stats()
		stats.game_active = True

		#重置记分牌图像
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()


		# 清空外星人列表和子弹列表  
		aliens.empty()
		bullets.empty()

		# 创建一群新的外星人
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()





# 重构: 响应按键按下
def check_keydown_events(event, ai_settings,screen,ship,bullets,stats):
	"""重构: 响应按键按下"""
	if event.key == pygame.K_RIGHT:
		# 将飞船的moving_right 标志位设为True
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

	elif event.key ==pygame.K_SPACE:
		#发射子弹
		fire_bullet(ai_settings,screen,ship,bullets)
	# 按下q退出游戏
	elif event.key == pygame.K_q:
		save_game_score(stats)#保存游戏记录
		sys.exit()	



# 重构: 响应按键松开

def check_keyup_events(event, ai_settings,screen,ship,bullets):
	"""响应按键松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key ==pygame.K_LEFT:
		ship.moving_left = False


def update_screen(ai_settings, screen, stats,sb,ship,aliens,bullets,play_button):
	"""更新屏幕界面,更新屏幕图像,并切换到新的屏幕"""
	# 每次循环都需要重新绘制屏幕
	screen.fill(ai_settings.bg_color)
	# 在飞船和外星人后面绘制所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen)

	# 显示得分面板
	sb.show_score()

	# 如果游戏处于非活动状态,绘制Play按钮
	if not stats.game_active:
		play_button.draw_button()

	# 让新绘制的屏幕可见
	pygame.display.flip()


# 提取子弹更新函数- 检查子弹与汪星人的碰撞
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
	"""更新子弹位置,删除消失的子弹"""
	bullets.update()
	# 删除消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	print(len(bullets))

	# 检查是否有子弹击中外星人
	# 若果有,则删除响应的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)


	# 子弹击中外星人,分数增加
	if collisions:
		for aliens in collisions.values():
			stats.score +=ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)

	# 创建新的外星人群
	if len(aliens) == 0 :
		# 删除现有的子弹,并新创建一群外星人
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, ship, aliens)
		#提高等级
		stats.level+=1
		sb.prep_level()

# 发射子弹
def fire_bullet(ai_settings,screen,ship,bullets):
	#创建一个子弹,并加入到bullets中
	if len(bullets)< ai_settings.bullets_allowed :#限制子弹数量
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)




# 创建外星人群
def create_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人群"""
	# 创建一个外星人,并计算一行可以容纳多少个
	# 外星人的间隔为外星人的宽度
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width

	##获取一行可以创建的外星人的个数
	number_aliens_x = get_number_aliens_x(ai_settings,alien_width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)


	# 创建多行外星人

	for row_number in range(number_rows):
		# 创建第一行外星人
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)


# 获取一行可以创建的外星人的个数

def get_number_aliens_x(ai_settings,alien_width):
	avilable_space_x = ai_settings.screen_width - 2* alien_width
	number_aliens_x = int(avilable_space_x/(2*alien_width))
	return number_aliens_x


# 创建指定行的第i个外星人
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""创建一个外星人,并放在当前行"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width+2*alien_width*alien_number
	alien.rect.x = alien.x

	# 设置飞船的y坐标
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

	aliens.add(alien)




# 计算屏幕能容纳的外星人飞船的行数

def get_number_rows(ai_settings,ship_height,alien_height):
	"""计算屏幕可以容纳外星人飞船的行数"""
	available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(available_space_y/(2*alien_height))
	return number_rows




# 外星人移动 - 检查是否有外星人位于边缘
def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
	"""更新外星人位置"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	# 检查飞船和外星人间的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)

	# 检查是否有外星人达到屏幕底端
	check_aliens_bottom(ai_settings, stats, screen,sb, ship, aliens, bullets)


def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets):
	"""响应飞船和外星人碰撞"""
	# 判断游戏是否可以继续进行

	if stats.ships_left > 0:
		# 将ships_left -1 
		stats.ships_left -=1 # 玩家可用飞船个数-1

		# 更新剩余可用飞船数
		sb.prep_ships()

		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		# 创建一群新的外星人,并将飞船放到屏幕底部中央
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()


		# 暂停
		sleep(0.5)
		
	else:
		stats.game_active = False
		
		# 光标可见
		pygame.mouse.set_visible(True)



# 检查,如果有外星人到达边缘是,改变移动方向,并向下移动外星人
def check_fleet_edges(ai_settings,aliens):
	"""有外星人到达边缘时,采取相应措施"""
	for alien in aliens.sprites():
		if alien.check_fleet_edges():
			change_fleet_direction(ai_settings,aliens)
			break

def change_fleet_direction(ai_settings,aliens):
	"""将整群外星人下移,并改变左右移动方向"""
	for alien  in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *=-1


def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets):
	"""检查是否有外星人达到屏幕底端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# 与飞船碰撞左同样处理
			ship_hit(ai_settings, stats, screen,sb, ship, aliens, bullets)
			break



def check_high_score(stats,sb):
	"""检查是否诞生了最高分"""
	if stats.score>stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()



import json
def save_game_score(stats): 
	"""保存游戏最高分"""
	data = {}
	data["high_score"] = stats.high_score
	with open("game_data.json",'w') as fobj:
		json.dump(data, fobj)

def read_game_score(stats):
	"""读取游戏最高记录得分"""
	file_name = "game_data.json"

	try:
		with open(file_name) as fobj:
			data = json.load(fobj)
			if data:
				high_score = data["high_score"]
				stats.high_score = high_score
				print(high_score)
	except FileNotFoundError:
		print("no high_score recored")

	






































