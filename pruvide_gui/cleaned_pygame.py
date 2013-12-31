import pygame, sys, os
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from text_pygame import TextPygame

#Colors
BLACK = (0,0,0)
WHITE = (250,250,250)

# Button to pin mappings
UP    = 23
DOWN  = 4
MENU  = 22
ENTER = 18

PINS = [ UP, DOWN, MENU, ENTER ]
#Draw Locations
TOP_LEFT        = (5,5)
TOP_MIDDLE      = (50,10)
CENTER_MIDDLE   = (50,50)
BOTTOM_CENTER   = (50,100)

set_point    = { 'text' : "63", 'draw_location' : (20,50), 'textpos' : (), 'color' : BLACK}
current_temp = { 'text' : "Temp: 63C", 'draw_location' : (10,70), 'textpos' : (), 'color' : BLACK}
menu         = { 'text' : "Set Temp: 66C", 'draw_location' : (10,100), 'textpos' : (), 'color' : BLACK}

set_point_object     = TextPygame("65", TOP_MIDDLE, BLACK, "Set Temp:")
current_temp_object  = TextPygame("55", CENTER_MIDDLE, BLACK, "Curr Temp:")
menu_object          = TextPygame("Menu", TOP_LEFT, BLACK)
temp_temp_object     = TextPygame("0", BOTTOM_CENTER, BLACK, "Set Temp:")

all_temps = [set_point, current_temp, menu]

def run_on_button_interrupt(pin):
  print pin
  if pin == UP:
    test = int(set_point['text']) + 1
    set_point['text'] = str(test)
    draw_all()
  if pin == DOWN:
    test = int(set_point['text']) - 1
    set_point['text'] = str(test)
    draw_all()

def initiate_buttons():
  for pin in PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=run_on_button_interrupt, bouncetime=300)

def render_and_draw_text(text):
  color = text['color']
  textpos = text['textpos']
  word = font.render(text['text'], True, color)
  if textpos:
    pygame.draw.rect(screen,WHITE,textpos)
    pygame.display.update()
  textpos = screen.blit(word,text['draw_location'])
  text['textpos'] = textpos
  pygame.display.update()


def draw_all():
  for i in all_temps:
    render_and_draw_text(i)

pygame.init()
screen = pygame.display.set_mode((120,160))
screen.fill(WHITE)
pygame.display.update()
font = pygame.font.Font(None, 30)
initiate_buttons()

while True:
  draw_all()
