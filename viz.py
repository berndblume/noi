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
  FLYDELAY = 0.1

  def __init__(self):
    # Must init self.max for use in command line bounds checking
    self.s = c.initscr()
    self.h, self.w = self.s.getmaxyx()
    self.max = min(self.h-2, (self.w - 2*Viz.SPC - 1) // (3*Viz.RPT))
    self.halfRpt = Viz.RPT // 2
    c.endwin()

  def __mkCenteredWin(self, n):
    self.wd = 3*n*Viz.RPT + 2*Viz.SPC
    yo = (self.h-n) // 2
    xo = (self.w - self.wd) // 2
    self.win = c.newwin(n+2, self.wd+1, yo, xo)

  def __status(self, str):
    self.win.addstr(self.size+1, 0, f"{str:^{self.wd}}")

  def __showPuck(self, y, x, w, offset=0):
    fill = Viz.HIDE*(self.halfRpt*(self.size-w))
    self.win.addstr(self.size-y, (Viz.RPT*self.size + Viz.SPC)*x+offset, fill + Viz.SHOW*Viz.RPT*w + fill)

  def __hidePuck(self, y, x, offset=0):
    self.win.addstr(self.size-y, (Viz.RPT*self.size + Viz.SPC)*x+offset, Viz.HIDE*Viz.RPT*self.size)

  def __animate(self, delay=0):
    self.win.refresh()
    if delay == 0:
      delay = Viz.DELAY / self.size
    sleep(delay)

  def __nextMove(self):
    # Uncomment if hide cursor not working
    # self.win.addstr(0, 3*self.size*Viz.RPT + 2*Viz.SPC, "")
    self.__status(f"{self.done:,}/{self.total:,} {100*self.done//self.total}%")
    self.done += 1
    self.win.refresh()
    # self.win.getkey()

  def __fly(self, grab, drop, w):
    if grab < drop:
      for o in range(0, (Viz.RPT*self.size + Viz.SPC) * (drop-grab)):
        self.__hidePuck(self.size, grab, o)
        self.__showPuck(self.size, grab, w, o+1)
        self.__animate(Viz.FLYDELAY / self.size)
    else:
      for o in range(0, (Viz.RPT*self.size + Viz.SPC) * (drop-grab), -1):
        self.__hidePuck(self.size, grab, o)
        self.__showPuck(self.size, grab, w, o-1)
        self.__animate(Viz.FLYDELAY / self.size)
    self.__hidePuck(self.size, drop)
    self.__animate(Viz.FLYDELAY / self.size)

  def __vizTowers(self, t):
    for n, w in enumerate(t.towers[0]):
      self.__showPuck(n, 0, w)
    self.__nextMove()
    for grab, drop in t.moves:
      w = t.towers[grab][-1]
      for h in range(len(t.towers[grab])-1, self.size):
        self.__hidePuck(h, grab)
        self.__showPuck(h+1, grab, w)
        self.__animate()
      self.__fly(grab, drop, w)
      t.apply(grab, drop)
      for h in range(self.size, len(t.towers[drop])-1, -1):
        self.__hidePuck(h, drop)
        self.__showPuck(h-1, drop, w)
        self.__animate()
      self.__nextMove()

  def __tModeOn(self):
    self.s = c.initscr()
    c.noecho()
    c.cbreak()
    c.curs_set(0) # Hide cursor
    self.s.keypad(True)

  def __tModeOff(self):
    self.s.keypad(False)
    c.curs_set(1) # Show cursor
    c.nocbreak()
    c.echo()
    c.endwin()

  def run(self, t):
    self.__tModeOn()
    self.size = t.size
    self.total = len(t.moves)
    self.done = 0
    self.__mkCenteredWin(self.size)
    try:
      self.__vizTowers(t)
    except:
      self.__tModeOff()
      raise
    self.win.getkey()
    self.__tModeOff()
