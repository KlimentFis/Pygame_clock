from random import randint
from datetime import datetime
import pygame

class Clock_face():
	def __init__(self, app):
		self.time = "start"
		self.all_char = {
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
			':' : [(1,1), (1,3)],
			"s" : [(0,0), (0,1), (0,2), (0,4), (1,0), (1,2), (1,4), (2,0), (2,2), (2,3), (2,4)],
			"t" : [(0,0), (1,0), (2,0), (1,1), (1,2), (1,3), (1,4)],
			"a" : [(1,0), (1,2), (0,1), (0,2), (0,3), (0,4), (2,1), (2,2), (2,3), (2,4)],
			"r" : [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,2), (1,3), (2,0), (2,1), (2,2), (2,4)]
		}
		self.chars = [Time_char(app, i, self.all_char[char]) for i, char in enumerate(self.time)]

	def draw(self):
		[char.draw(app) for char in self.chars]

	def update(self):
		self.time = datetime.now().strftime("%H:%M")
		[char.update(self.all_char[self.time[i]]) for i, char in enumerate(self.chars)]

class Time_char():
	def __init__(self, app, i, char):
		self.x = (app.row - (app.element_count*3 + app.element_count + 1)) // 2 + (1 * (i+1) + i * 3) 
		self.y = (app.col - 7)//2 + 1
		chanel = lambda: randint(40, 220)
		self.color = (chanel(), chanel(), chanel()) 
		self.char = char

	def draw(self, app):
		# Rainbow 1
		[pygame.draw.rect(app.display, (255 // app.row * (self.x + x1), 255 // app.col * (self.y + y1), 255 // app.width // app.height * (self.x + x1) * (self.y + y1)), ((self.x + x1) * app.cell_size + 1, (self.y + y1) * app.cell_size + 1, app.cell_size - 2, app.cell_size - 2)) for x1, y1 in self.char]
		# Rainbow 2
		# [pygame.draw.rect(app.display, (255 // app.row * self.x, 255 // app.col * (self.y + 6), 255 // app.width // app.height * (self.x + x1) * (self.y + y1)), ((self.x + x1) * app.cell_size + 1, (self.y + y1) * app.cell_size + 1, app.cell_size - 2, app.cell_size - 2)) for x1, y1 in self.char]
		# Random color 
		# [pygame.draw.rect(app.display, self.color, ((self.x + x1) * app.cell_size + 1, (self.y + y1) * app.cell_size + 1, app.cell_size - 2, app.cell_size - 2)) for x1, y1 in self.char]

	def update(self, char):
		self.char = char

class App():
	def __init__(self):
		self.cell_size = 20
		self.element_count = 5
		self.row = 21 #self.element_count * 3 + self.element_count + 1
		self.col = 7 #7
		self.width = self.cell_size * self.row
		self.height = self.cell_size * self.col
		self.display = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()

	def run(self):
		My_clock = Clock_face(self)
		while True:
			self.clock.tick(15)
			self.display.fill(pygame.Color("black"))
			My_clock.draw()
			My_clock.update()
			pygame.display.update()
			[exit() for i in pygame.event.get() if i.type == pygame.QUIT]

if __name__ == '__main__':
	app = App()
	app.run()
