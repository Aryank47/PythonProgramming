# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:55:19 2019

@author: Aryan Kumar
"""

from private import employee
from private import findsum

ep = employee()
ep.set("e1")
ep.get()

import private

e = private.employee()
e.set("Aryan")
e.get()





e = findsum()
e.setvalue(10031231, 34341312312)
e.getsum()
# e.print(__a) illegal access
