#!/usr/bin/env python3

from viz import Viz
from towers import Towers
from rdargs import rdargs

v = Viz()
t = Towers(rdargs(v))
v.run(t)
