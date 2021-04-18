#!/usr/bin/env python3

class Twr:

  def __init__(self, n):
    self.size = n
    self.towers = [[*range(n, 0, -1)], [], []]
    self.moves = [(0, 1), (0, 2), (1, 2)]

  def apply(self, grab, drop):
    self.towers[drop].append(self.towers[grab].pop())
