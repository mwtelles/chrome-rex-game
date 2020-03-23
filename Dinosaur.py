import pygame


class Dinosaur(pygame.sprite.Sprite):
	def __init__(self, WIDTH=640, HEIGHT=500):
		pygame.sprite.Sprite.__init__(self)
		self.HEIGHT = HEIGHT
		self.WIDTH = WIDTH
		# self.imgs = ['./images/dinosaur/wait.png', './images/dinosaur/afraid.png', './images/dinosaur/running.png', './images/dinosaur/flying.png']
		self.imgs = ['./images/dinosaur/dino.png', './images/dinosaur/dino_ducking.png']
		self.reset()

	def jump(self, time_passed):
		# time_passed
		if self.is_jumping_up:
			self.rect.top -= self.jump_v * time_passed
			self.jump_v = max(0, self.jump_v - self.jump_a_up * time_passed)
			if self.jump_v == 0:
				self.is_jumping_up = False
		else:
			self.rect.top = min(self.initial_top, self.rect.top + self.jump_v * time_passed)
			self.jump_v += self.jump_a_down * time_passed
			if self.rect.top == self.initial_top:
				self.is_jumping = False
				self.is_jumping_up = True
				self.jump_v = self.jump_v0

	def be_afraid(self):
		self.dinosaur = self.dinosaurs.subsurface((352, 0), (88, 95))

	def draw(self, screen):
		if self.is_running and not self.is_jumping:
			self.running_count += 1
			if self.running_count == 6:
				self.running_count = 0
				self.running_flag = not self.running_flag
			if self.running_flag:
				self.dinosaur = self.dinosaurs.subsurface((176, 0), (88, 95))
			else:
				self.dinosaur = self.dinosaurs.subsurface((264, 0), (88, 95))
		screen.blit(self.dinosaur, self.rect)

	def reset(self):

		self.is_running = False

		self.running_flag = False
		self.running_count = 0

		self.is_jumping = False

		self.is_jumping_up = True

		self.jump_v0 = 500

		self.jump_v = self.jump_v0

		self.jump_a_up = 1000
		self.jump_a_down = 800

		self.initial_left = 40
		self.initial_top = int(self.HEIGHT/2.3)
		self.dinosaurs = pygame.image.load(self.imgs[0]).convert_alpha()
		self.dinosaur = self.dinosaurs.subsurface((0, 0), (88, 95))
		self.rect = self.dinosaur.get_rect()
		self.rect.left, self.rect.top = self.initial_left, self.initial_top