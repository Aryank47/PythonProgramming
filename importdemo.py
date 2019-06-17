# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:18:01 2019

@author: Aryan Kumar
"""


class employee:
    __name = ""

    def set(self, name):
        self.__name = name

    def get(self):
        print(self.__name)



class findsum:
    __a = __b = 0

    def setvalue(self, a, b):
        self.__a = a
        self.__b = b

    def getsum(self):
        print(self.__a + self.__b)
