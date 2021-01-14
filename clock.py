import pygame
from datetime import datetime


pygame.init()
size = 20
# color = (255, 0, 0) #Red 
# color = (0, 255, 0) #Green
# color = (0, 0, 255) #Blue
color = (255, 255, 255) #White
# color = (0, 255, 255) #Aqua
# color = (255, 255, 0) #Yellow
# color = (66, 170, 255) #WhiteBlue
width = (3 * 5 + 6) * size 
height = 7 * size

display = pygame.display.set_mode((width, height))

char = {
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
}

def draw(x, y, i, color):
	pygame.draw.rect(display, color, (x * size + (size * 1) + i * size * 4, y * size + (size * 1), size, size))



Game_over = False
while not Game_over:
	time = datetime.now().strftime("%H:%M")

	for i in range(width):
		for j in range(height):
			draw(i, j, 0, (0, 0, 0))

	for i in range(5):
		for x in range(width):
			for y in range(height):
				if (x, y) in char[time[i:i+1]]:
					draw(x, y, i, color)

	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Game_over = True


pygame.quit()