#!/usr/bin/env python3

# Vizualizer in its own class to simplify plugging other visualizers than curses

import curses as c
from time import sleep
from towers import Towers

class Viz:
  SHOW = '█'
  HIDE = ' '
  RPT = 2 # How many repeated characters per puck width increment; must be a multiple of 2
  SPC = 2 # Space between tower racks
  MIN = 2 # Min Rack height allowed for this visualization
  max = 4 # Max Rack size - will be calculated based on screen size
  min = MIN
  DELAY = 0.2 # Seconds to wait in animations

  def __init__(self):
    # Must init self.max for use in command line bounds checking
    self.s = c.initscr()
    self.h, self.w = self.s.getmaxyx()
    self.max = min(self.h-1, (self.w - 2*Viz.SPC - 1) // (3*Viz.RPT))
    self.halfRpt = Viz.RPT // 2

  def __mkCenteredWin(self, n):
    wd = 3*n*Viz.RPT + 2*Viz.SPC
    yo = (self.h-n) // 2
    xo = (self.w - wd) // 2
    self.win = c.newwin(n+1, wd+1, yo, xo)

  def __showPuck(self, y, x, w):
    fill = Viz.HIDE*(self.halfRpt*(self.size-w))
    self.win.addstr(self.size-y, (Viz.RPT*self.size + Viz.SPC)*x, fill + Viz.SHOW*Viz.RPT*w + fill)

  def __hidePuck(self, y, x):
    self.win.addstr(self.size-y, (Viz.RPT*self.size + Viz.SPC)*x, Viz.HIDE*Viz.RPT*self.size)

  def __nextMove(self):
    self.win.addstr(0, 0, "")
    self.win.refresh()
    self.win.getkey()

  def __vizTowers(self, t):
    for n, w in enumerate(t.towers[0]):
      self.__showPuck(n, 0, w)
    self.__nextMove()
    for grab, drop in t.moves:
      self.__hidePuck(len(t.towers[grab])-1, grab)
      t.apply(grab, drop)
      self.__showPuck(len(t.towers[drop])-1, drop, t.towers[drop][-1])
      self.__nextMove()

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
    self.size = t.size
    self.__mkCenteredWin(self.size)
    try:
      self.__vizTowers(t)
    except:
      self.__tModeOff()
      raise
    self.__tModeOff()
