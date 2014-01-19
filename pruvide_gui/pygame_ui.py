import pygame, sys, os
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from text_pygame import TextPygame
import zmq
import time
import json
from ui_state_machine import UiStateMachine
from menu_system import MenuSystem

#zmq subscribe
sub_context = zmq.Context()
sub_socket = sub_context.socket(zmq.SUB)
sub_socket.connect("tcp://127.0.0.1:6000")
sub_socket.setsockopt(zmq.SUBSCRIBE, '')

#zmq req
req_context = zmq.Context()
req_socket = req_context.socket(zmq.REQ)
req_socket.connect("tcp://127.0.0.1:5000")

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
SET_POINT       = (10,20)
CURRENT_TEMP    = (30,20)
CURRENT_TIME    = (50,20)

def welcome_screen():
  welcome_word = TextPygame("Welcome to PruVide", screen, CURRENT_TIME, font = 20, textpos = (85,10,15,130))
  image = pygame.image.load("/home/pi/all_projects/pru_vide/pruvide_gui/images/cooking_ingredients.jpg")
  image_rotated = pygame.transform.rotate(image,90)
  imagepos = image_rotated.get_rect()
  screen.blit(image_rotated,(0,20,80,120))
  welcome_word.render_and_draw()
  pygame.display.update()


def run_on_button_interrupt(pin):
  print pin
  setpoint_send = ''
  if pin == UP:
    set_point.up_one()
    set_point.render_and_draw()
  if pin == DOWN:
    set_point.down_one()
    set_point.render_and_draw()
  if pin == ENTER:
    response = ''
    to_send = json.dumps({ 'setpoint' : set_point.text })
    req_socket.send(to_send)
    response = req_socket.recv()
    print "i hit enter"
    if response:
      print "I'm in if response"
      render_and_draw_text(setp)
      render_and_draw_text(set_point)
      print response

def clear_screen():
  screen.fill(WHITE)
  pygame.display.update()

def initiate_buttons():
  for pin in PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=run_on_button_interrupt, bouncetime=300)

def draw_all():
  for i in all_temps:
    i.render_and_draw()

def check_state_on_button_interrupt(pin):
  my_state = some_state.current_state
  if my_state == 'main_menu':
    if pin == UP:
      my_menu.up_menu()
      my_menu.draw_menu()
    elif pin == DOWN:
      my_menu.down_menu()
      my_menu.draw_menu()
    elif pin == ENTER:
      menu_state_map[my_menu.return_current()]()

  if my_state == 'setting_setpoint':
    if pin == UP:
      temporary_temp.up_one()
      temporary_temp.render_and_draw()
    elif pin == DOWN:
      temporary_temp.down_one()
      temporary_temp.render_and_draw()
    elif pin == ENTER:
      menu_state_map['send_temperature']

    elif pin == MENU:

# Init screen and buttons
pygame.init()
screen = pygame.display.set_mode((120,160))
screen.fill(WHITE)
pygame.display.update()
font = pygame.font.Font(None, 26)
initiate_buttons()

set_point = TextPygame("50", screen, SET_POINT, prefix = "Setpoint: ", textpos = ())
current_temp = TextPygame("70", screen, CURRENT_TEMP, prefix = "Temp: ", textpos = ())
current_time = TextPygame("0", screen, CURRENT_TIME, prefix = "Time(min): ", textpos = ())
temporary_temp = TextPygame("50", screen, SET_POINT, prefix = "", textpos = ())
all_temps = [  set_point, current_temp, current_time]

menu = {'Set Temp': '50', 'Pre-sets': {'beef' : '140', 'fish': '65', 'veggies': '100' },
        'Config': {'Device': 'Rice Cooker', 'Probe': '28-0000000000'} }

some_state = UiStateMachine()
my_menu = MenuSystem(screen, menu_level(menu))

def menu_level(full_menu):
  level = []
  for k,v in full_menu.items():
    level.append(v)
  return level

def send_setpoint():
    response = ''
    to_send = json.dumps({ 'setpoint' : temporary_temp.text })
    req_socket.send(to_send)
    response = req_socket.recv()
    print "i hit enter"
    if response:
      print "I'm in if response"
      clear_screen()
      set_point.text = temporary_temp.text
      set_point.render_and_draw()
      print response
    my_menu.send_temperature()

def to_setpoint():
  my_menu.set_setpoint()
  clear_screen()
  temporary_temp.text = set_point.text
  temporary_temp.render_and_draw()

def to_preset():
  my_menu.set_preset()
  my_menu.set_new_menu(menu_level(menu[my_menu.return_current()]))
  my_menu.draw_menu()

def to_config():
  my_menu.set_config()
  menu_level(menu[my_menu.return_current()])

def cancel_setpoint():
  my_menu.cancel()
  temporary_temp.text = ""
  my_menu.draw_menu()

menu_state_map = { 'Set Temp': to_setpoint, 'Pre-sets': to_preset,
    'send_temperature': send_setpoint, 'Config': to_config, 'cancel': cancel_setpoint }

welcome_screen()
time.sleep(2)
clear_screen()

while True:
  sub = sub_socket.recv()
  my_dict = json.loads(sub)
  print my_dict
  if my_dict:
    current_temp.set_text( my_dict['temp'][0:4])
    current_time.set_text( my_dict['time'][0:3])
  draw_all()
