import time
import sys
import os
import pygame


red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

class rectObj:
	xCoord = 0
	color = red
#center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'
#window size
(width, height) = (2560, 300)
screen_color = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
screen.fill(screen_color)
pygame.display.set_caption('Optokinetic Tape Test')
pygame.display.flip()


#create 29 blocks to add to the list
numBlocks = int((width-60)/100)+5
blockList = []

count = 0
toggle = 0
# 0 -> red
# 1 -> black
for x in range(numBlocks):
    tempBlock = rectObj()

    if toggle == 0 :
        tempBlock.xCoord = (x*100)-100
        toggle = 1
        blockList.append(tempBlock)
        continue

    if toggle == 1 :
        tempBlock.xCoord = (x*100)-100
        tempBlock.color = black
        count += 1
        blockList.append(tempBlock)
        #create 4 black blocks for every 1 red
        if count == 4 :
            count = 0
            toggle = 0

#debugging for list size
print("LENGTH")
print(len(blockList))
for x in range(len(blockList)):
	print(x, " ", blockList[x].xCoord, blockList[x].color)

#create surface to create green rectangle
surf = pygame.Surface((400,150))
surf.fill((255,255,255))
pygame.draw.rect(surf, green, (0, 0, 400, 150), 7)
#place at this pixel location
screen.blit(surf, (1080, 75))

blockFile = open("blockPos.txt", "w")
eyeFile = open("eyePos.txt", "w")


running = True
speed = 2
runs = 0
forward = 1
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#sets num runs in each direction and flips direction when needed
	if runs == 1000:
		if forward == 0:
			running = False
		runs = 0
		forward = 0
	if forward == 0:
		if speed > 0:
			time.sleep(.5)
			speed = speed*(-1)

#want to track when block in in xCoords 350 - 650
	tempBlock = rectObj()
	for block in blockList:
		pygame.draw.rect(screen, block.color, (block.xCoord, 100, 100, 100))

		#if block visible inside region
		if block.xCoord > 980 and block.xCoord < 1480 and block.color == red:
			tempBlock.xCoord = block.xCoord

		block.xCoord += speed
		if block.xCoord == 2900:
			block.xCoord = -100
		if block.xCoord == -200:
			block.xCoord = 2800


        #sleep needed to fine tune speed depending on system
	time.sleep(.005)
	pygame.display.update()
	mouseX,mouseY = pygame.mouse.get_pos()
	updateTime = time.perf_counter_ns()


	#blockFile.write("Block in Focus Zone at Coords:\n")
	#block can be partially in the region from the left, fully enclosed or partially in from the right side
	if tempBlock.xCoord  < 1080 and tempBlock.xCoord  > 980:
		blockFile.write("%i%s%i %s %i\n" % (1080, ",", (tempBlock.xCoord+100), "at time:", updateTime))
	elif tempBlock.xCoord > 1380 and tempBlock.xCoord  < 1480:
		blockFile.write("%i%s%i %s %i\n" % (tempBlock.xCoord, ",", 1480, "at time:", updateTime))
	elif tempBlock.xCoord  < 1480 and tempBlock.xCoord  >= 1080:
		blockFile.write("%i%s%i %s %i\n" % (tempBlock.xCoord, ",", (tempBlock.xCoord+100), "at time:", updateTime))

	eyeFile.write("%i%s%i %s %i\n" % (mouseX, ",", mouseY, "at time:", updateTime))
	#print(mouseX,mouseY)

	runs += 1
