import pygame, sys, os
os.environ["SDL_FBDEV"] = "/dev/fb1"

BLACK = (0,0,0)
WHITE = (250,250,250)

pygame.init()
screen = pygame.display.set_mode((120,160))
screen.fill(WHITE)
pygame.display.update()

def welcome_screen():
  font_welcome = pygame.font.Font(None, 20)
  word = pygame.transform.rotate(font_welcome.render("Welcome to PruVide", True, BLACK), 90)
  set_point = pygame.transform.rotate(font_welcome.render("Choose a Temp: 65C", True, BLACK), 90)
  image = pygame.image.load("images/cooking_ingredients.jpg")
  image_rotated = pygame.transform.rotate(image,90)
  imagepos = image_rotated.get_rect()
  screen.blit(image_rotated,(0,20,80,120))
  screen.blit(word, (85,10,15,130))
  screen.blit(word, (100,10,15,130))
  pygame.display.update()

welcome_screen()
