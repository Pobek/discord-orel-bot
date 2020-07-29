class Config(object):
  CURSES_EN = []
  ANSWERS_EN = []
  CURSES_HE = []
  ANSWERS_HE = []

  def __repr__(self):
    rt = ""
    for key, value in self.__dict__.items():
      rt += f'\'{key}\':{value}, '
    return rt