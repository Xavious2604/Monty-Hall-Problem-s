import pygame
import random
pygame.init()
white = (255, 255, 255)
X = 1200
Y = 650
doors = random.sample(range(1, 4), 3)
goat1 = doors[0]
goat2 = doors[1]
goats = [goat1, goat2]
car = doors[2]
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Simulation')
image = pygame.image.load('D:/Project/Python/Project 5/all_doors.jpg')
change = False
msg_disp = False


def music():
	file = 'D:/Project/Python/Project 5/click.mp3'
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()


def show_car(car, state):
	my_font = pygame.font.SysFont("latoblack", 26)
	display_surface = pygame.display.set_mode((X, Y))
	car1 = pygame.image.load('D:/Project/Python/Project 5/car_1.jpg')
	car2 = pygame.image.load('D:/Project/Python/Project 5/car_2.jpg')
	car3 = pygame.image.load('D:/Project/Python/Project 5/car_3.jpg')

	if car == 1:
		display_surface.blit(car1, (0, 0))
		pygame.display.update()
	elif car == 2:
		display_surface.blit(car2, (0, 0))
		pygame.display.update()
	elif car == 3:
		display_surface.blit(car3, (0, 0))
		pygame.display.update()
	if state == 1:
		the_text = my_font.render("You won by switching!",
								True, (231, 0, 10))
		display_surface.blit(the_text, (350, 180))
		pygame.display.update()
	elif state == 2:
		the_text = my_font.render(
			"You could've won by staying!", True,
		(231, 0, 0))
		display_surface.blit(the_text, (350, 180))
		pygame.display.update()
	elif state == 3:
		the_text = my_font.render("You won by staying!", 
								True, (231, 0, 0))
		display_surface.blit(the_text, (350, 180))
		pygame.display.update()
	elif state == 4:
		the_text = my_font.render(
			"You could've won by switching!", True,
		(231, 0, 0))
		display_surface.blit(the_text, (350, 180))
		pygame.display.update()


def draw_rect():
	pygame.draw.rect(display_surface, (20, 24, 11), 
					(300, 220, 300, 40), 1)
	pygame.display.update()
	pygame.draw.rect(display_surface, (14, 2, 200), 
					(300, 260, 300, 40), 1)
	pygame.display.update()


while True:
	music()
	if change == False:
		display_surface.fill(white)
		display_surface.blit(image, (0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

		pygame.display.update()

		clicked = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			# Check if door 1 is pressed.
			if(event.pos[0] >= 71 and event.pos[0] <= 203
			and event.pos[1] >= 387 and event.pos[1] <= 632):
				user = 1
				clicked = True
				music()
			# Check if door 2 is pressed.
			elif(event.pos[0] >= 353 and event.pos[0] <= 485
				and event.pos[1] >= 386 and event.pos[1] <= 635):
				user = 2
				clicked = True
				music()
			# Check if door 3 is pressed.
			elif(event.pos[0] >= 938 and event.pos[0] <= 1100
				and event.pos[1] >= 387 and event.pos[1] <= 633):
				user = 3
				
				clicked = True
				music()
		if clicked:

			image1 = pygame.image.load('D:/Project/Python/Project 5/goat_1.jpg')
			image2 = pygame.image.load('D:/Project/Python/Project 5/goat_2.jpg')
			image3 = pygame.image.load('D:/Project/Python/Project 5/goat_3.jpg')
			image4 = pygame.image.load('D:/Project/Python/Project 5/car_1.jpg')
			image5 = pygame.image.load('D:/Project/Python/Project 5/car_2.jpg')
			image6 = pygame.image.load('D:/Project/Python/Project 5/car_3.jpg')
			wr = random.randint(0, 1)
			if(goats[0] == user):
				g = goats[1]
			elif(goats[1] == user):
				g = goats[0]
			else:
				g = goats[wr]
			if g == 1:
				change = True
				display_surface.blit(image1, (0, 0))
				pygame.display.update()
			elif g == 2:
				change = True
				display_surface.blit(image2, (0, 0))
				pygame.display.update()
			elif g == 3:
				change = True
				display_surface.blit(image3, (0, 0))
				pygame.display.update()
			print(u"There is a goat behind door {}".format(g))

			my_font = pygame.font.SysFont("mvboli", 26)
			the_text = my_font.render("Do you want to:", True, (231, 0, 0))
			display_surface.blit(the_text, (350, 180))
			the_text2 = my_font.render("1.Switch", True, (0, 0, 190))
			display_surface.blit(the_text2, (350, 220))
			the_text3 = my_font.render("2.Stay", True, (190, 0, 0))
			display_surface.blit(the_text3, (350, 260))
			draw_rect()
			clicked2 = False
			print(u"The car is behind door {}".format(car))

	# for event in pygame.event.get():
		clicked2 = False
		if event.type == pygame.MOUSEBUTTONDOWN:
		
			# Compare click coordinates with coordinates
			# where it says 'Switch' and 'Stay'.
			if(event.pos[0] >= 299 and event.pos[0] <= 597
			and event.pos[1] >= 220 and event.pos[1] <= 260):
				
				# user2 = 1 means user has chosen to switch.
				user2 = 1
				clicked2 = True
			elif(event.pos[0] >= 301 and event.pos[0] <= 598
				and event.pos[1] >= 259 and event.pos[1] <= 297):
			
				# user2 = 2 means user has chosen to stay.
				user2 = 2
				clicked2 = True

		if clicked2:

			if user2 == 1:
				print("You chose to switch!")
				if user in goats:
					my_font = pygame.font.SysFont("mvboli", 26)
					the_text = my_font.render(
						"You won by switching!", True, (231, 0, 0))
					state = 1
					display_surface.blit(the_text, (350, 180))
					pygame.display.update()
					print("You won by switching!")
					
				# User has chosen the door behind which there is a car.
				else: 
					my_font = pygame.font.SysFont("mvboli", 26)
					the_text2 = my_font.render(
						"You could've won by staying!", True, (231, 0, 0))
					state = 2
					display_surface.blit(the_text2, (350, 180))
					pygame.display.update()
					print("You could have won by switching!")
			elif user2 == 2:
				print("You chose to stay!")
				if user == car:
					my_font = pygame.font.SysFont("mvboli", 26)
					the_text3 = my_font.render(
						"You won by staying!", True, (231, 0, 0))
					display_surface.blit(the_text3, (350, 180))
					state = 3
					pygame.display.update()
					print("You won by staying!")
				else:
					my_font = pygame.font.SysFont("mvboli", 26)
					the_text4 = my_font.render(
						"You could've won by switching!", True, (231, 0, 0))
					display_surface.blit(the_text4, (350, 180))
					state = 4
					pygame.display.update()
					print("You could have won by switching!")
			show_car(car, state)
