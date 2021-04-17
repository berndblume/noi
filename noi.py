#!/usr/bin/env python3

import curses as c
import sys

class Viz:
  CHR = '*'
  RPT = 2
  SPC = 2
  MIN = 2
  max = 4
  min = MIN

  def __init__(self, s):
    self.s = s
    self.h, self.w = s.getmaxyx()
    self.max = min(self.h, (self.w - 2*Viz.SPC) // Viz.RPT)
    s.clear()

  def prep(self, n):
    yo = (self.h-n) // 2
    xo = (self.w - 3*n*Viz.RPT - 2*Viz.SPC) // 2
    self.win = c.newwin(self.h, self.w, yo, xo)

  def tst(self):
    self.win.addstr(0, 0, "Hi.")
    self.win.refresh()
    self.win.getkey()


def noi(s):
  DEF = 4
  v = Viz(s)
  a = sys.argv[1:]
  if len(a) != 1:
    n = DEF
  else:
    n = int(a[0])
    if n < v.min:
      n = v.min
    if n > v.max:
      n = v.max
  v.prep(n)
  t = [range(n, 0, -1), [], []]
  v.tst()

c.wrapper(noi)
