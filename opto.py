import time
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
pygame.display.set_caption('Optokinetic Tape Test')
pygame.display.flip()



numBlocks = int(width/100)+2
blockList = []

count = 0
toggle = 0
# 0 -> red
# 1 -> black
for x in range(numBlocks):
    tempBlock = rectObj()

    if toggle == 0 :
        tempBlock.xCoord = x*100
        toggle = 1
        blockList.append(tempBlock)
        continue

    if toggle == 1 :
        tempBlock.xCoord = x*100
        tempBlock.color = black
        count += 1
        blockList.append(tempBlock)
        if count == 3 :
            count = 0
            toggle = 0

for blocks in blockList:
    blocks.xCoord -= 100


#for block in blockList:
	#pygame.draw.rect(screen, block.color, (block.xCoord, 100, 100, 100))

#pygame.draw.rect(screen, red, (-50, 100, 100, 100))
green = (0,255,0)

surf = pygame.Surface((300,150))
surf.fill((255,255,255))
pygame.draw.rect(surf, green, (0, 0, 300, 150), 7)
screen.blit(surf, (350, 75))

blockFile = open("blockPos.txt", "w")
eyeFile = open("eyePos.txt", "w")


running = True
speed = 5
runs = 0
forward = 1
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	if runs == 500:
		if forward == 0:
			running = False
		runs = 0 
		forward = 0

	if forward == 0:
		if speed > 0:
			time.sleep(.5)
			speed = speed*(-1)

#want to track when block in in xCoords 350 - 650
	for block in blockList:
		pygame.draw.rect(screen, block.color, (block.xCoord, 100, 100, 100))


		if block.xCoord > 250 and block.xCoord < 650:
			blockFile.write("Block in Focus Zone at Coords:\n")
			blockFile.write("%i %s %i\n" % (block.xCoord, "to", (block.xCoord+100)))	
													

		block.xCoord += speed
		if block.xCoord == 1100:
			block.xCoord = -100
		if block.xCoord == -200:
			block.xCoord = 1000
		print(block.xCoord)
													
        #sleep needed to fine tune speed depending on system
	time.sleep(.005)			
	pygame.display.update()




	v,f = pygame.mouse.get_pos()
	#print(v,f)
	runs += 1
