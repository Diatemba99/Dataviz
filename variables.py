#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:50:50 2021

@author: diatemba
"""

a = 4
b = 1.5
c = True

print(a)
print(b)

f = lambda x,y: x**2 + y**2

print(f(5,4))

def calcul_energie(masse, hauteur, g):
    energie = masse * hauteur * g
    print(energie, "joules")
    return energie
    

print("Hello guys")    
resultat = calcul_energie(50, 14, 9.81)