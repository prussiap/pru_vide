import pygame, sys, os
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from menu_system import MenuSystem
import zmq
import time

#zmq subscribe
#sub_context = zmq.Context()
#sub_socket = sub_context.socket(zmq.SUB)
#sub_socket.connect("tcp://127.0.0.1:6000")
#sub_socket.setsockopt(zmq.SUBSCRIBE, "menu")

#zmq req
#req_context = zmq.Context()
#req_socket = req_context.socket(zmq.REQ)
#req.connect("tcp://127.0.0.1:6000")

#Colors
BLACK = (0,0,0)
WHITE = (250,250,250)

# Button to pin mappings
UP    = 23
DOWN  = 27
MENU  = 22
ENTER = 18

PINS = [ UP, DOWN, MENU, ENTER ]

#Draw Locations
TOP_LEFT        = (5,5)
TOP_MIDDLE      = (50,5)
CENTER_MIDDLE   = (70,70)
BOTTOM_CENTER   = (50,140)

pygame.init()
screen = pygame.display.set_mode((120,160))
screen.fill(WHITE)
pygame.display.update()

def welcome_screen():
  font_welcome = pygame.font.Font(None, 20)
  word = pygame.transform.rotate(font_welcome.render("Welcome to PruVide", True, BLACK), 90)
  image = pygame.image.load("images/cooking_ingredients.jpg")
  image_rotated = pygame.transform.rotate(image,90)
  imagepos = image_rotated.get_rect()
  screen.blit(image_rotated,(0,20,80,120))
  screen.blit(word, (85,10,15,130))
  pygame.display.update()

def clear_screen():
  screen.fill(WHITE)
  pygame.display.update()

clear_screen()

menu = {'Set Temp': '50', 'Pre-sets': {'beef' : '140', 'fish': '65', 'veggies': '100' },
        'Config': {'Device': 'Rice Cooker', 'Probe': '28-0000000000'} }

my_menu = MenuSystem(screen, menu)
my_menu.draw_menu()
my_menu.return_current()
time.sleep(1)
my_menu.up_menu()
my_menu.draw_menu()
my_menu.return_current()
time.sleep(1)
