import pygame
import random
pygame.init()

win = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake")

screenWidth = 600
objectWidth = 15
score = 0

class fruit:
	def __init__(self, objectWidth, screenWidth):
		self.positions = []
		self.x = objectWidth *random.randint(2, (screenWidth//objectWidth) - 2)
		self.y = objectWidth *random.randint(2, (screenWidth//objectWidth) - 2)
		self.width = objectWidth
		self.height = objectWidth
		
	def draw(self):
		pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))



class snake:
	def __init__(self, x, y, objectWidth):
		self.x = x
		self.y = y
		self.width = objectWidth
		self.height = objectWidth
		self.speed = objectWidth
		self.direction = "left"
		self.lastDirection = "right"

	def draw(self):
		pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, self.width, self.height))

	def move(self):
		if self.direction == "left" and self.lastDirection != "right":
			player.left()
			self.lastDirection = "left"

		elif self.direction == "right" and self.lastDirection != "left":
			player.right()
			self.lastDirection = "right"


		elif self.direction == "up" and self.lastDirection != "down":
			player.up()
			self.lastDirection = "up"


		elif self.direction == "down" and self.lastDirection != "up":
			player.down()
			self.lastDirection = "down"

		else:
			if self.lastDirection == "left":
				player.left()

			if self.lastDirection == "right":
				player.right()

			if self.lastDirection == "up":
				player.up()

			if self.lastDirection == "down":
				player.down()


	def left(self):
			self.x -= self.speed

	def right(self):
		self.x += self.speed

	def up(self):
		self.y -= self.speed
	
	def down(self):
		self.y += self.speed


def checkMovement():
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			player.direction = "left"

		elif keys[pygame.K_RIGHT]:
			player.direction = "right"

		elif keys[pygame.K_UP]:
			player.direction = "up"

		elif keys[pygame.K_DOWN]:
			player.direction = "down"

def collisionWithFruit():
	# move fruit
	f.x = objectWidth *random.randint(2, screenWidth//objectWidth - 2)
	f.y = objectWidth *random.randint(2, screenWidth//objectWidth - 2)
	global score
	score += 1
	print("score = {}".format(score))
	print(f.x, f.y)

def checkCollisionWithFruit():
	if f.x == player.x and f.y == player.y:
		collisionWithFruit()

def checkCollisionsWithTail():
	for x, y in tail.lastPositions:
		if x == player.x and y == player.y:
			global score
			score = 0
			player.x = 450
			player.y = 300
			tail.lastPositions = []
			pygame.time.delay(300)
			f.x = objectWidth *random.randint(2, screenWidth//objectWidth - 2)
			f.y = objectWidth *random.randint(2, screenWidth//objectWidth - 2)

def checkCollisionsWithEdge():
	global screenWidth
	if player.x < 0 or player.x >= screenWidth or player.y < 0 or player.y >= screenWidth:
		global score
		score = 0
		player.x = 450
		player.y = 300
		tail.lastPositions = []
		pygame.time.delay(300)
		f.x = objectWidth *random.randint(2, screenWidth//objectWidth - 2)
		f.y = objectWidth *random.randint(2, screenWidth//objectWidth - 2)

class snakeTail:
	def __init__(self, score, objectWidth):
		self.score = score
		self.objectWidth = objectWidth
		self.lastPositions = [] # [[x1, y1], [x2, y2]]

	def draw(self):
		for x, y in self.lastPositions:
			pygame.draw.rect(win, (0, 255, 0), (x, y, self.objectWidth, self.objectWidth))

	
f = fruit(objectWidth, screenWidth)
player = snake(450, 300, objectWidth)
tail = snakeTail(score, objectWidth)

run = True
while run:
	pygame.time.delay(100)
	#clears screen
	win.fill((0, 0, 0))
	# if you quit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# sends last positions
	if score > 0:
		tail.lastPositions.append([player.x, player.y])

		if len(tail.lastPositions) >= score * 6:
			
			tail.lastPositions.pop(0) # removes first element
	

	checkMovement()
	f.draw()
	player.move()
	player.draw()
	tail.draw()
	checkCollisionWithFruit()
	checkCollisionsWithTail()
	checkCollisionsWithEdge()

	pygame.display.update()



