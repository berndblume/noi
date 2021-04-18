#!/usr/bin/env python3

class Towers:

  def __mkMoves(self, n, grab, drop, via):
    if n <= 1:
      self.moves.append((grab, drop))
    else:
      self.__mkMoves(n-1, grab, via, drop)
      self.moves.append((grab, drop))
      self.__mkMoves(n-1, via, drop, grab)

  def __init__(self, n):
    self.size = n
    self.towers = [[*range(n, 0, -1)], [], []]
    self.moves = []
    print("Calculating moves...")
    self.__mkMoves(n, 0, 2, 1)
    print(f"Found solution with {len(self.moves):,} moves.")
    i = input("Hit Return to continue: > ")

  def apply(self, grab, drop):
    self.towers[drop].append(self.towers[grab].pop())
