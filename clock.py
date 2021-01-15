import pygame
from datetime import datetime
from time import sleep


pygame.init()

# Setings/Настройки
size = 30
bg_color = (0, 0, 0)
# color = (43, 255, 10)
# color = (255, 0, 0) #Red 
# color = (0, 255, 0) #Green
# color = (0, 0, 255) #Blue
# color = (255, 255, 255) #White
# color = (0, 255, 255) #Aqua
color = (255, 255, 0) #Yellow
# color = (66, 170, 255) #WhiteBlue

# Create display on setings template/ Создание дисплея на основе настроек
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
	pygame.draw.rect(display, color, (x * size + (size * 1) + i * size * 4 + 1, y * size + (size * 1) + 1, size-2, size-2))



Game_over = False
while not Game_over:
	time = datetime.now().strftime("%H:%M")

	# Fill background/ Заливка фона
	for i in range(width):
		for j in range(height):
			draw(i - 1, j - 1, 0, bg_color)

	# draw number/ Рисование чисел
	for i in range(5):
		for x in range(width):
			for y in range(height):
				if (x, y) in char[time[i:i+1]]:
					draw(x, y, i, color)

	# Update display/ Обновление дисплея
	pygame.display.update()

	# Tick effect/ Эффект тиканья
	draw(9, 1, 0, bg_color)
	draw(9, 3, 0, bg_color)
	sleep(0.5)

	pygame.display.update()

	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Game_over = True


pygame.quit()
