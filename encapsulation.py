# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:12:56 2019

@author: Aryan Kumar
"""
import sys

'''
class test:
    x=10
    __y=100;#private variable declaration
    def disp(self):
        print("Fuck")
        
t=test()
print(t.x)
#print(t.y)# illegal access




class student:
    def display(self,name=None):
        if len(name)<= 5:
            print('Fuck off')
        else:
            print(name," Fuck off")
            
s=student()
s.display('chodu')




var="fuck off"
print(var.capitalize())
print(var.replace('f','Z'))
print(var.upper())
print(var[0])

'''
print(sys.platform)
print("Enter the strings:")
s1 = input()
s2 = s1[::-1]
if s1 == s2:
    print("Palindrome")
else:
    print("Not Palindrome")
