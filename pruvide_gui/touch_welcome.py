#!/usr/bin/python
# touchv6
# Texy 5/12/13

import pygame, sys, os, time
from pygame.locals import *
from text_pygame import TextPygame
from button import Button
from evdev import InputDevice, list_devices
devices = map(InputDevice, list_devices())
eventX=""
for dev in devices:
  if dev.name == "ADS7846 Touchscreen":
    eventX = dev.fn
print eventX

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
os.environ["SDL_MOUSEDEV"] = eventX
pygame.init()
                # set up the window
screen = pygame.display.set_mode((320,240), 0, 32)
pygame.display.set_caption('Drawing')


# set up the colors
COLORS = dict(
  BLACK = (  0,   0,   0),
  WHITE = (255, 255, 255),
  RED   = (255,   0,   0),
  GREEN = (  0, 255,   0),
  BLUE  = (  0,   0, 255),
  CYAN  = (  0, 255, 255),
  MAGENTA=(255,   0, 255),
  YELLOW =(255, 255,   0)
)

screen.fill(COLORS['WHITE'])
pygame.display.update()

def clear_screen():
  screen.fill(WHITE)
  pygame.display.update

def one_item(default_settings):
  blah = TextPygame(**default_settings)
  blah.render_and_draw()
  return blah

def draw_rect(location, width):
  rect = pygame.draw.rect(screen, BLACK, location, width)
  pygame.display.te()
  return rect

top_center = (70, 70, 180, 50)
center_center = (70, 120, 180,50)
rect_row1_col1 = (50,10,50,150)
ect_row1_col2 = (50,160,50,150)
row1_dim = (50, 10, 60, 300)
row2_dim = (110, 10, 60, 300)
row3_dim = (170, 10, 60, 300)


start_text = dict(text="Start", screen=screen, font=50)
a_button = Button(center_center, start_text)
a_button.render_and_draw()


start_text2 = dict(text="Quit", screen=screen, font=50)
a_button2 = Button(top_center, start_text2)
a_button2.render_and_draw()
#draw_rect(rect_row1_col1, 2)
#draw_rect(rect_row1_col2, 2)
time.sleep(2)
#row1x1rect = ct(center_center, 2)
#a_rect = pygame.Rect(center_center)
#print a_rect.centerx
#print a_rect.centerya
#start_text = dict(text="Start", screen=screen, textpos=a_rect, font=50)
#start_text2 = dict(text="Quit", screen=screen, textpos=(), font=50)
#row1x1text = one_item(start_text)
# Display some text
#font = pygame.font.Font(None, 36)
#text = font.render("Touch here to quit", 1, (BLACK))
                #text = pygame.transform.rotate(text,270)
#textpos = text.get_rect(centerx=background.get_width()/2,centery=background.get_height()/2)
#background.blit(text, textpos)

#screen.blit(background, (0, 0))
#pygame.display.flip()

#---------
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
#      if row1x1text.does_collide(pygame.mouse.get_pos()):
        print "veryy cool"
#        clear_screen()
#        running = False
#  pygame.display.update()
#------
                # run the game loop
#while running:
#  for event in pygame.event.get():
#    if event.type == QUIT:
#      pygame.quit()
#      sys.exit()
#      running = False
#    elif event.type == pygame.MOUSEBUTTONDOWN:
#      print("Pos: %sx%s\n" % pygame.mouse.get_pos())
#      if textpos.collidepoint(pygame.mouse.get_pos()):
#        pygame.quit()
#        sys.exit()
#        running = False
#    elif event.type == KEYDOWN and event.key == K_ESCAPE:
#      running = False
#  pygame.display.update()
