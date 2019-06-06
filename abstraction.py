# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:30:58 2019

@author: Aryan Kumar
"""

from abc import ABC, abstractmethod


class car(ABC):
    def xxx(self):
        print("xxxx")

    @abstractmethod
    def stop(self):
        pass


class driver(car):
    def stop(self):
        print("Stop")


d = driver()
d.stop()
d.xxx()
