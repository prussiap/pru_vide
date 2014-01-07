import pygame, sys, os
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from text_pygame import TextPygame
import zmq
import time
import json

#zmq subscribe
sub_context = zmq.Context()
sub_socket = sub_context.socket(zmq.SUB)
sub_socket.connect("tcp://127.0.0.1:6000")
sub_socket.setsockopt(zmq.SUBSCRIBE, '')

#zmq req
#req_context = zmq.Context()
#req_socket = req_context.socket(zmq.REQ)
#req_socket.connect("tcp://127.0.0.1:6000")

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
CENTER_MIDDLE   = (60,80)
CENTER_MID_BEL  = (60,90)
BOTTOM_CENTER   = (60,150)
SETP            = (10,60)
SET_POINT       = (10,20)
CURRENT_TEMP    = (30,20)
CURRENT_T       = (30,60)
CURRENT_TIME    = (50,20)
CURRENT_TI      = (50,60)


set_point    = { 'text' : "50", 'draw_location' : SET_POINT, 'textpos' : (), 'color' : BLACK}
setp         = { 'text' : "Setpoint:", 'draw_location' : SETP, 'textpos' : (), 'color' : BLACK}
current_temp = { 'text' : "63", 'draw_location' : CURRENT_TEMP, 'textpos' : (), 'color' : BLACK}
current_t    = { 'text' : "Temp: ", 'draw_location' : CURRENT_T, 'textpos' : (), 'color' : BLACK}
current_time = { 'text' : "100", 'draw_location' : CURRENT_TIME, 'textpos' : (), 'color' : BLACK}
current_ti   = { 'text' : "Time (min): ", 'draw_location' : CURRENT_TI, 'textpos' : (), 'color' : BLACK}
menu         = { 'text' : "200", 'draw_location' : (10,100), 'textpos' : (), 'color' : BLACK}

#set_point_object     = TextPygame("65", CENTER_MID_BEL, BLACK, "Set Temp:")
#current_temp_object  = TextPygame("55", CENTER_MIDDLE, BLACK, "Curr Temp:")

all_temps = [ setp, set_point, current_temp, current_time, current_t, current_ti]

def welcome_screen():
  font_welcome = pygame.font.Font(None, 20)
  word = pygame.transform.rotate(font_welcome.render("Welcome to PruVide", True, BLACK), 90)
  image = pygame.image.load("/home/pi/all_projects/pru_vide/pruvide_gui/images/cooking_ingredients.jpg")
  image_rotated = pygame.transform.rotate(image,90)
  imagepos = image_rotated.get_rect()
  screen.blit(image_rotated,(0,20,80,120))
  screen.blit(word, (85,10,15,130))
  pygame.display.update()

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
  if pin == ENTER:
    response = ""
    set_point = set_point['text']
    print set_point
    render_and_draw_text(setp)
    render_and_draw_text(set_point)

 #   rep_socket.send(set_point)
 #   while response == "":
 #     response = rep_socket.recv()
 #     if response:
 #       render_and_draw_text(setp)
 #       render_and_draw_text(set_point)
 #       print response

def initiate_buttons():
  for pin in PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=run_on_button_interrupt, bouncetime=300)

def render_and_draw_text(text):
  color = text['color']
  textpos = text['textpos']
  word = pygame.transform.rotate(font.render(text['text'], True, color),90)
  if textpos:
    pygame.draw.rect(screen,WHITE,textpos)
    pygame.display.update()
  textpos = screen.blit(word,text['draw_location'])
  text['textpos'] = textpos
  pygame.display.update()


def clear_screen():
  screen.fill(WHITE)
  pygame.display.update()

def draw_all():
  for i in all_temps:
    render_and_draw_text(i)

# Init screen and buttons
pygame.init()
screen = pygame.display.set_mode((120,160))
screen.fill(WHITE)
pygame.display.update()
font = pygame.font.Font(None, 26)
initiate_buttons()

welcome_screen()
time.sleep(2)
clear_screen()

while True:
  sub = sub_socket.recv()
  my_dict = json.loads(sub)
  print my_dict
  if my_dict:
    current_temp['text'] = my_dict['temp'][0:4]
    current_time['text'] = my_dict['time'][0:3]
    set_point['text']    = my_dict['set_point'][0:4]
  draw_all()
