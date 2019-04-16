import time
import sys
import os
import pygame
import random


red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

class rectObj:
	xCoord = 0
	color = red

#center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'
#window size
(width, height) = (2560, 1060)
screen_color = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Random Test')
screen.fill(screen_color)
pygame.display.flip()


blockFile = open("RandBlockPos.txt", "w")
eyeFile = open("RandEyePos.txt", "w")

x = 0
y = 0
runTimes = 10
z = 0
block = rectObj()
while(z < runTimes):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			z = runTimes
	preX = x
	preY = y
	x = random.randint(10,2401)
	if x == preX:
		x = random.randint(10,2401)
	y = random.randint(10, 981)
	if y == preY:
		y = random.randint(10,981)
	pygame.draw.rect(screen, block.color, (x, y, 100, 100))
	pygame.draw.rect(screen, (255,255,255), (preX, preY, 100, 100))
	time.sleep(1)
	pygame.display.update()
	mouseX,mouseY = pygame.mouse.get_pos()
	updateTime = time.perf_counter_ns()
	blockFile.write("%s%i%s%s%i%s %s %i\n" % ("X: ",x+50, " +- 50, ", "Y: ", y+50, " +- 50 ", "at time:", updateTime))
	eyeFile.write("%s%i%s%i %s %i\n" % ("X: ", mouseX,', Y: ', mouseY,"at time:", updateTime))

	z += 1
