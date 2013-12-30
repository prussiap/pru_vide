class TextPygame:
  def __init__(self, text,  screen_location, color, prefix = "", textpos = ()):
    self.text = text
    self.screen_location = screen_location
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

