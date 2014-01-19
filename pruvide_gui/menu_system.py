import pygame, sys, os
from pygame.locals import *
from text_pygame import TextPygame
from collections import deque
import time
import itertools

class MenuSystem:
  def __init__(self, screen, menu_items, font = 24):
    self.screen = screen
    self.font_size = font
    self.current_item = 0
    self.font = pygame.font.Font(None, font)
    self.centerx = 30
    self.starty = 15
    self.menu_objects = deque()
    self.menu_items = deque(menu_items)
    self.padding = 5
    self.make_menu_objects()

  def place_carrot(self):
    pos = self.menu_objects[0].textpos
    x = pos[0]
    y = pos[1] + pos[3]
    self.carrot = TextPygame(">", self.screen, (x,y) , prefix = "", textpos = ())

  def make_menu_objects(self):
    self.menu_objects = deque()
    currenty = self.starty
    self.menu_objects.append(TextPygame(self.menu_items[0], self.screen, (currenty, self.centerx),
      prefix = "", textpos = ()))
    for item in itertools.islice(self.menu_items, 1, len(self.menu_items)):
      currenty = (self.font_size/2) + currenty + self.padding
      self.menu_objects.append(TextPygame(item, self.screen,
            (currenty, self.centerx) , prefix = "", textpos = ()))

  def return_current(self):
    print self.menu_items[0]

  def up_menu(self):
    self.menu_items.rotate(-1)
    self.make_menu_objects()

  def down_menu(self):
    self.menu_items.rotate(1)
    self.make_menu_objects()

  def clear_screen(self):
    self.screen.fill((250,250,250))
    pygame.display.update()

  def draw_menu(self):
    self.clear_screen()
    for item in self.menu_objects:
      item.render_and_draw()
    self.place_carrot()
    self.carrot.render_and_draw()
#    time.sleep(4)
