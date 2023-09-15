# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:21:14 2023

@author: wilkijam
"""

# Benefits of a project folder
    # All of your code and files that you create or use are centralized
    # you don't have to worry about super long file paths

# Commenting in python:
    # The # precedes any comment
    # in spyder you can hit CTRL 1

print('Hello World!') # this will print hello world    

#%% Section Breaks

# A special type of comment that makes your code easier to run and
# navigate

#%%% This is a Subsection

# Comment

#%% Shortcuts in Spyder

# 1) Ribbon
# 2) Keyboard shortcuts (hover over for those keyboard shortcuts)
    # Full list: Tools -> Preferences -> Keyboard Shortcuts
# F9 -> Runs a single line
# CTRL + Enter -> Runs a cell (or section)
# F5 -> Runs your entire .py file

#%% Data types & numerical value

# Types of data in Python
    # 1) Numerical
    # 2) Strings
    
# Numerical Data Types:
    # 1) Numbers 
    # 2) Dates
    
# Within numbers, there are two main types:
    # 1) Integer
    # 2) Floats
    
# To create variables
x = 5
y = 2.2

type(x)

# You don't need to declare variables in Python

z = 5
# Recast variable to a different data type
z = float(z)

num = x + y
num = int(num)

#%% Strings & string methods

x = 'Hi'
y = "Hello"
# Python doesn't care if you use single or double quotes to wrap strings

# For multi-line strings, prefix & suffix the string with 3 single quotes

mLString = '''
This
is
a
multi
line
string'''

# Print simply prints information to the CONSOLE
print(mLString)

firstName = 'Jamie'
firstname = 'Other Jamie'
# Case sensitivity matters in VARIABLE NAMES -> these are two separate variable

del firstname # Deletes a variable from memory
# Otherwise you can right click in var explorer or use the trash can

'Example' == 'example'
# even in a string, case sensitivity matter

# In python you concatenate strings with +

firstName = 'Jamie'
lastName = 'Wilkie'

print(firstName + ' ' + lastName)

player = 'Wayne Gretzky'
pNum = 99

print(player + "'s number is "+ pNum)
print(player + "'s number is "+ str(pNum))
# you can't concatenate numericals with strings

player * 5
# In python multiplication on strings repeats

mktCap = '$123,789'
mktCap * 12
int(mktCap) * 12
# we can't cast to integer because of the $ and the ,

# String methods
myName = 'Jamie Wilkie'
print(myName.upper())
# General syntax matters to apply methods:  object.method(arguments)
# Most common string methods are on page 18

# Where can we get a list of all methods?
dir(myName)

# If you are trying to understand a method or function
help(print)

# Slicing strings
# Maybe I want the first char, last char, char 12-29
greeting = 'Hello World'

# In python we can retrieve 'slices' of information using index number
greeting[0:5]
# Get me the characters from index 0 (inclusive) to index 5 (exclusive)
greeting[:5]
# if you exclude the first index it starts at the beginning

greeting[6:]
greeting[-5:]
# negative numbers will count from the END when slicing
greeting[-1]

#%% Lists & list methods

# Lists are a 1D array
# Lists can hold any type of data
    # Numbers, strings, lists
    # one list can have MULTIPLE data types within it
# listName = [item1, item2, item3]

list1 = ['a', 'b', 'c']
list2 = [1, 'b', 3.5]
list3 = ['w', list2, 7]

# Retriving info from lists:
    # Use slices just like with string
print(list1[1])    
print(list1[0:2])

# List (when added to another list) are linked
# Making changes to a list:
list2[1] = 'c'

list3[1][0]
list3[1][0] = 15

# List method:
    # Adding onto a list with .append()
    
list1 = ['a', 'b', 'c']
list1.append('d')

list1.append(['e', 'f'])

list1 = ['a', 'b', 'c']
list1.append('d')

# extend method
# you give it an iterable and it will add each item to the end fo the list
list1.extend(['e', 'f'])


# Lists are mutable
# .insert() method

list1.insert(2, ['x', 'y'])

# .remove method
# Removes a particular item from a list
    # only removes the first occurence of the item

list1 = ['a', 'b', 'c']
list1.remove('b')

list2 = ['a', 'b', 'c', 'a', 'b', 'c']
list2.remove('b')

# .pop method
# you specify an index number and it will remove that item from the list
list1 = ['a', 'b', 'c']
list1.pop(1) # pop also RETURNS the removed item
removed = list1.pop() # if you don't provide an index it removes the last item in list

# .sort
list1 = ['a', 'b', 'c','e', 'd']
list1.sort()
list1.sort(reverse=True)
# the sort method changes the list in place

#%% Dictionaries

# Dictionaries store items in key: value pairs
# Key: like the index (it's used to retrieve items from the dict)
# Value: a piece of data associated with a unique key
# dictName = {key1: val1, key2: val2, ...}

dict1 = {'AAPL': 140, 'NFLX': 600, 'TSLA': 790}

# Accessing a dict -> similar to lists, but use the key instead of indes
print(dict1['AAPL'])

# Modifying is just like with a list
dict1['AAPL'] = 250

dict1 = {'AAPL': 140, 'NFLX': 600, 'TSLA': 790, 'NFLX': 900}
# with duplicated keys, the value will be the LAST value entered for key

dict1['MSFT'] = 130
# Once your dictionary is created you can add as many new key value pairs
# as you want

dict2['MSFT'] = 250

dict2 = {} #You must initialize before you can add
dict2['MSFT'] = 250

# .pop to remove items from a dictionary

dict1.pop('MSFT')

# displaying a dictionary
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

#%% Tuples

# A tuple is a lot like a list
    # Tuples are IMMUTABLE -> you can't change individual items
tuple1 = (1, 2, 3)
tuple1[1] = 150 # error because we can't modify individual items
tuple1 = (1, 150, 3)

#%% Logical operators in Python

# Standard logical operators -> return TRUE / FALSE
5 == 9 # checks equivalency (in Excel =)
5 != 9 # checks inequivalency (in Excel <>)
# >, <, >=, <= are all the same as Excel

# Not Logic
# Flip the logic from TRUE -> FALSE or v/v
not(5==9)

# And logic
(5>3 and 5>5)

# Or logic
(5>3 or 5>5)

# Bitwise operators
    # Bitwise AND: &
    # Bitwise OR: |
    # Avoid these in general python code, they may give you unexpected results
    
#%% Conditional statement

a = 1
if a > 1:
    print('a is greater than 1')
elif a < 2:
    print('a is less than 2')
elif a < 3:
    print('a is less than 3')
else:
    print('a is greater than or equal to 3')

if 5==5: print('5 is equal to 5')

#%% For loops

# Loop the code a defined (known) number of times
# Syntax:
    # for varName in iterable:
        # code to execute

# To iterate a fixed number of times use the RANGE() function to generate
# an iterable

for j in range(5): # from zero to x-1
    print(j)
    
for j in range(5, 15): # from x to y-1
    print(j)
    
for j in range(5, 15, 2): # from x to y-step, counting by step
    print(j)
    
list1 = [1, 5, 3, 4]
for j in list1:
    print(j**2) # exponents in python are **    
    
dict1 = {'A': 1, 'B': 3, 'C': 7}

#%% Do while loop

# Syntax:
    # while condition:
        # code to execute
        
i = 0
while i < 5:
    print(i)
    i += 1