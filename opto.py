import sys
import pygame


red = (255,0,0)
black = (0,0,0)

class rectObj:
	xCoord = 0
	color = red

(width, height) = (1000, 300)
screen_color = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
screen.fill(screen_color)
pygame.display.flip()



numBlocks = int(width/100)+2
blockList = []

for x in range(numBlocks):
		tempBlock = rectObj()
		if x == 0:
			tempBlock.xCoord = -100
		else:
			if x%2 == 1:
				tempBlock.color = black
				tempBlock.xCoord = 100*(x-1)
			else:
				tempBlock.xCoord = 100*(x-1)
		blockList.append(tempBlock)


#for block in blockList:
	#pygame.draw.rect(screen, block.color, (block.xCoord, 100, 100, 100))

#pygame.draw.rect(screen, red, (-50, 100, 100, 100)) 

running = True
speed = 2

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	for block in blockList:
		pygame.draw.rect(screen, block.color, (block.xCoord, 100, 100, 100))
		block.xCoord += speed
		if block.xCoord == 1100:
			block.xCoord = -100

				
	pygame.display.update()
