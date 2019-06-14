# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:55:19 2019

@author: Aryan Kumar
"""

from private import employee

ep = employee()
ep.set("Chodu")
ep.get()

import private

e = private.employee()
e.set("Aryan")
e.get()

import math

print(math.pow(2, 100))
print(dir(math))

from private import findsum

e = findsum()
e.setvalue(10031231, 34341312312)
e.getsum()
# e.print(__a)
