import pygame, sys, os
from pygame.locals import *
from text_pygame import TextPygame
from collections import deque
import time
import itertools

class Button:
  def __init__(self, rect_pos, text_dict):
    self.screen = text_dict['screen']
    self.rect_pos = rect_pos
    self.rect = self.draw_rect(rect_pos)
    self.text_object = TextPygame(**text_dict)
    self.calculate_and_set_text_center()

  def draw_rect(self, location):
    rect = pygame.draw.rect(self.screen, (0,0,0), location, 2)
    pygame.display.update()
    return rect

  def render_and_draw(self):
    self.text_object.render_text()
    self.text_object.draw_text()

  def calculate_and_set_text_center(self):
    textx, texty = self.text_object.get_text_size()
    newx = self.rect_pos[0] + (textx/2)
    newy = self.rect_pos[1] + 10
    self.text_object.set_screen_location((newx,newy))


