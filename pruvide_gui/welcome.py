import pygame, sys, os
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from text_pygame import TextPygame
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


fun_text = TextPygame("hello", screen, TOP_LEFT, prefix = "World", textpos = ())
font = pygame.font.Font(None, 25)
#choose_setpoint = TextPygame("25", screen, TOP_MIDDLE, BLACK, 20)

#welcome_screen()
#time.sleep(1)
clear_screen()
#time.sleep(6)
fun_text.render_and_draw()
time.sleep(3)
fun_text.set_text("china")
fun_text.render_and_draw()
time.sleep(3)
