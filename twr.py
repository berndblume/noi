#!/usr/bin/env python3

class Twr:

  def __init__(self, n):
    self.size = n
    self.towers = [range(n, 0, -1), [], []]
