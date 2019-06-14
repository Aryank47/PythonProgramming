# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:34:07 2019

@author: Aryan Kumar
"""

import math as m

# print(dir(m))

n = int(input("Enter a number: "))
print(m.factorial(n))

n1 = int(input("Entera number: "))
res = 0
while n1 != 0:
    res += n1
    n1 -= 1

print(res)

s1 = ""
s1 = input("Enter a string:")
i = input("Enter the character: ")
count = j = 0
for i in s1:
    if i == s1[j]:
        count += 1

print(count)
