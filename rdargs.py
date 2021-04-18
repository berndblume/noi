#!/usr/bin/env python3

from viz import Viz

# Read number of pucks from command line.
# If not given, not numeric or out of range, use max possible for screen size
def rdargs(v):
  import sys
  a = sys.argv[1:]
  if len(a) != 1:
    n = v.max
  else:
    try:
      n = int(a[0])
    except:
      n = v.max
    if n < v.min:
      n = v.min
    if n > v.max:
      n = v.max
  return n
