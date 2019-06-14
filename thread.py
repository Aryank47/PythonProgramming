# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 14:53:03 2019

@author: Aryan Kumar
"""

import threading


class student(threading.Thread):
    __name = []
    y = ""

    def display(self):
        print(self.__name)

    def run(self):
        for x in range(4):
            y = input("Enter your name: ")
            self.__name.append(y)


x = student()
x.start()
x.join()
x.display()
