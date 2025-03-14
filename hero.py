import pygame 

class Hero(object):
	def __init__(self, screen):
		super(Hero, self).__init__()
		self.screen = screen # this gives the hero the ability to control the screen

		# loading the image
		self.image = pygame.image.load('images/hero.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect() 

		self.rect.centerx = self.screen_rect.centerx 
		self.rect.bottom = self.screen_rect.bottom 

		self.moving_right = False #sets up the movement of booleans
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	# this updates all the hero in the class
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += 10 #moves  the hero to right
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= 10 #moves the hero to left
		elif self.moving_up and self.rect.top > self.screen_rect.top:
			self.rect.y -= 10 #moves the hero up
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += 10 #moves the hero down	

	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect)