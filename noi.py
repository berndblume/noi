#!/usr/bin/env python3

from viz import Viz
from twr import Twr
from rda import rdargs

v = Viz()
t = Twr(rdargs(v))
v.run(t)
