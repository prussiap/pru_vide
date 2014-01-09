import pygame, sys, os
from pygame.locals import *
class TextPygame:
  def __init__(self, text, screen,  screen_location, color = (0,0,0), font = 26 , prefix = "", textpos = ()):
    self.text = text
    self.screen_location = screen_location
    self.font = pygame.font.Font(None, font)
    self.screen = screen
    self.textpos = textpos
    self.color = color
    self.prefix = prefix

  def set_text(self, text):
    self.text = text

  def up_one(self):
    foo = float(self.text) + 1
    self.text = str(foo)

  def down_one(self):
    foo = float(self.text) - 1
    self.text = str(foo)

  def set_screen_location(self, location):
    self.screen_location = location

  def set_textpos(self, pos):
    self.textpos = pos

  def form_text(self):
    return self.prefix +' ' + self.text

  def render_and_draw(self):
    word = pygame.transform.rotate(self.font.render(self.form_text(), True, self.color), 90)
    if self.textpos:
      pygame.draw.rect(self.screen, (255,255,255), self.textpos)
    self.textpos = self.screen.blit(word,self.screen_location)
    pygame.display.update()
