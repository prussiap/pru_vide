import pygame, sys, os
from pygame.locals import *
class TextPygame:
  def __init__(self, text, screen,  screen_location, color, font = 0 , prefix = "", textpos = ()):
    self.text = text
    self.screen_location = screen_location
    if font:
      self.font = pygame.font.Font(None, font)
    else:
      self.font = pygame.font.Font(None, 26)
    self.screen = screen
    if textpos:
      self.textpos = textpos
    self.color = color
    if prefix:
      self.prefix = prefix

  def set_text(self, text):
    self.text = text

  def set_screen_location(self, location):
    self.screen_location = location

  def set_textpos(self, pos):
    self.textpos = pos

  def form_text(self):
    return self.prefix +' ' + self.text

  def render_and_draw(self):
    word = pygame.transform.rotate(self.font.render(self.text, True, self.color), 90)
    if self.textpos:
      pygame.draw.rect(screen,WHITE,self.textpos)
      pygame.display.update()
    self.textpos = screen.blit(word,self.screen_location)
    self.textpos = textpos
    pygame.display.update()
