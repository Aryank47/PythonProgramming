# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:12:56 2019

@author: Aryan Kumar
"""
class student:
    def display(self,name=None):
        if len(name)<= 5:
            print('hello')
        else:
            print(name," hello")
            
s=student()
s.display('aryan')





