# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:17 2024

@author: bmaba
"""

import pandas

file=pandas.read_csv("country_data.csv")

print(file)
"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
"""

age=[30,25,29,46,22]

print(age)

"""
[30, 25, 29, 46, 22]
"""
#the first index is 0 not 1. for eexample what is the first age?
print(age[0])
"""
30
"""
print(min(age))
"""
22
"""
avg= sum(age)/len(age)
print(avg)
"""
30.4
"""

c1="South Africa"
c2="Lesotho"

print(age[0:2])
"""[30, 25]
Adding a number to a list use append
"""
age.append(100)
print(age)
"""
[30, 25, 29, 46, 22, 100]
"""