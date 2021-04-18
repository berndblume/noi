#!/usr/bin/env python3

# Vizualizer in its own class to simplify plugging other visualizers than curses

import curses as c
from twr import Twr

class Viz:
  CHR = '*'
  RPT = 2
  SPC = 2
  MIN = 2
  max = 4
  min = MIN

  def __init__(self):
    # Must init self.max for use in command line bounds checking
    self.s = c.initscr()
    self.h, self.w = self.s.getmaxyx()
    self.max = min(self.h, (self.w - 2*Viz.SPC) // (3*Viz.RPT))

  def __mkCenteredWin(self, n):
    yo = (self.h-n) // 2
    xo = (self.w - 3*n*Viz.RPT - 2*Viz.SPC) // 2
    self.win = c.newwin(self.h, self.w, yo, xo)

  def __vizTowers(self, t):
    self.win.addstr(0, 0, "Hi, " + str(t.size))
    self.win.refresh()
    self.win.getkey()

  def __tModeOn(self):
    c.noecho()
    c.cbreak()
    self.s.keypad(True)

  def __tModeOff(self):
    self.s.keypad(False)
    c.nocbreak()
    c.echo()
    c.endwin()

  def run(self, t):
    self.__tModeOn()
    self.__mkCenteredWin(t.size)
    try:
      self.__vizTowers(t)
    except:
      self.__tModeOff()
      raise
    self.__tModeOff()
