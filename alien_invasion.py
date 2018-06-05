import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alinen Invasion")

	#创建一个用于储存游戏统计信息的实例
	stats = GameStats(ai_settings)

	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	# 开始游戏的主循环
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
		gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()