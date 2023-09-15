# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:24:42 2023

@author: wilkijam
"""

#%% Assignment 1, Question 2

mktCap = '$123,456,789'

mktCap = mktCap.strip('$')
mktCap = mktCap.split(',')
mktCap = ''.join(mktCap)
mktCap = int(mktCap)
mktCap * 2

# What else could we use
mktCap = '$123,456,789'
mktCap = int(mktCap.replace('$', '').replace(',', ''))

#%% Assign 1, Q3

prices = [100, 99, 105, 110, 95, 102]

# Loop over all elements in the prices
for px in prices:
    if px > 102:
        print(f'The price is ${px:.2f} therefore, buy')
        # f string formatting is only available in Python > 3.6; so this 
        # could cause compatibility issues
    elif px < 100:
        print('The price is ' + str(px) + ' therefore, sell')
    else:
        print('The price is ' + str(px) + ' therefore, hold')
    
# For each item, check which category it belong in and print the result
    
