import pygame
from datetime import datetime
from time import sleep
from random import randint

pygame.init()

class Clock():
	def __init__(self):
		self.size = 30
		self.bg_color = (0, 0, 0)
		self.color = (255, 0, 0)
		self.width = (3 * 5 + 6) * self.size 
		self.height = 7 * self.size
		# self.flags = pygame.NOFRAME | pygame.RESIZABLE
		# self.display = pygame.display.set_mode((self.width, self.height), self.flags)
		self.display = pygame.display.set_mode((self.width, self.height))
		self.char = {
			'0' : [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,4), (2,0), (2,1), (2,2), (2,3), (2,4)],
			'1' : [(2,0), (2,1), (2,2), (2,3), (2,4)],
			'2' : [(0,0), (0,2), (0,3), (0,4), (1,0), (1,2), (1,4), (2,0), (2,1), (2,2), (2,4)],
			'3' : [(0,0), (0,2), (0,4), (1,0), (1,2), (1,4), (2,0), (2,1), (2,2), (2,3), (2,4)],
			'4' : [(0,0), (0,1), (0,2), (1,2), (2,0), (2,1), (2,2), (2,3), (2,4)],
			'5' : [(0,0), (0,1), (0,2), (0,4), (1,0), (1,2), (1,4), (2,0), (2,2), (2,3), (2,4)],
			'6' : [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,2), (1,4), (2,0), (2,2), (2,3), (2,4)],
			'7' : [(0,0), (1,0), (2,0), (2,1), (2,2), (2,3), (2,4)],
			'8' : [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,2), (1,4), (2,0), (2,1), (2,2), (2,3), (2,4)],
			'9' : [(0,0), (0,1), (0,2), (0,4), (1,0), (1,2), (1,4), (2,0), (2,1), (2,2), (2,3), (2,4)],
			':' : [(1,1), (1,3)]
		}

	def Draw(self, x, y, i, color):
		pygame.draw.rect(self.display, color, (x * self.size + (self.size * 1) + i * self.size * 4 + 1, y * self.size + (self.size * 1) + 1, self.size-2, self.size-2))


	def Draw_number(self):
		for i in range(len(self.time)):
			for x in range(self.width):
				for y in range(self.height):
					if (x, y) in self.char[self.time[i:i+1]]:	
						Clock.Draw(self, x, y, i, self.color)

	def Get_time(self):
		self.time = datetime.now().strftime("%H:%M")

	def Fill_display(self):
		self.display.set_colorkey(self.bg_color)

	def Tick(self):
		Clock.Draw(self, 9, 1, 0, self.bg_color)
		Clock.Draw(self, 9, 3, 0, self.bg_color)
		

Game_over = False
while not Game_over:

	my_clock = Clock()
	my_clock.Fill_display()
	my_clock.Get_time()
	my_clock.Draw_number()
	pygame.display.update()
	my_clock.Tick()
	sleep(1)
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Game_over = True


pygame.quit()
