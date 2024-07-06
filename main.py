from random import randint, choice
import pygame
from datetime import datetime
import pygame
import json

def get_settings():
	with open('settings.json', 'r') as file:
		data = json.load(file)

	clock_params = data.get("Clock", {})

	size = clock_params.get("Size")
	circle = clock_params.get("Circle")
	am = clock_params.get("AM")
	seconds = clock_params.get("Seconds")
	return (am, seconds, size)

class Clock_face():
	def __init__(self, app):
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
			"r" : [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,2), (1,3), (2,0), (2,1), (2,2), (2,4)],
			"m" : [(0,0), (0,1), (0,2), (0,3), (0,4), (1,1), (2,0), (2,1), (2,2), (2,3), (2,4)],
			"p" : [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,2), (2,0), (2,1), (2,2)],
			" " : []
		}

		if app.element_count % 2 == 1:
			self.time = " " * ((app.element_count - 5) // 2) + "start" + " " * ((app.element_count - 5) // 2)
		else:
			self.time = "".join([str(choice([i for i in self.all_char.keys()])) for i in range(app.element_count)])

		self.chars = [Time_char(app, i, self.all_char[char]) for i, char in enumerate(self.time)]

	def draw(self):
		[char.draw(app) for char in self.chars]

	def update(self):
		if SECONDS == 0:
			self.time = datetime.now().strftime("%M")
		else:
			self.time = datetime.now().strftime("%M:%S") 

		if USA_TIME_FORMAT == 0:
			self.time = datetime.now().strftime("%H:") + self.time
		else:
			self.time = datetime.now().strftime("%I:") + self.time + datetime.now().strftime(":%p").lower()

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
		self.cell_size = CELL_SIZE
		self.element_count = 5 + SECONDS * 3 + USA_TIME_FORMAT * 3
		self.row = self.element_count * 3 + self.element_count + 1 #21
		self.col = 9 #7
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
			pygame.display.update()
			My_clock.update()
			[exit() for i in pygame.event.get() if i.type == pygame.QUIT]

if __name__ == '__main__':
	# USA_TIME_FORMAT = 0  # 12h format with AM/PM (1 or 0)
	# SECONDS = 1  # seconds on the clock (1 or 0)
	# CELL_SIZE = 35

	USA_TIME_FORMAT, SECONDS, CELL_SIZE = get_settings()

	app = App()
	app.run()
