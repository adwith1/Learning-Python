# -*- coding: utf-8 -*-
"""Intermediate Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SOUO42gcjZjg2LZMe0GYOCbtwOxeLz3k

For Loops
"""

for i in range(0, 10, 2): #start, stop, step
  print(i)

"""Lists and Tuples"""

#A list is a collection of different data types
fruits = ['apple', 'orange', 'banana', 3]
print(fruits)
print(fruits[3])
fruits.append('kiwi')
print(fruits)

fruits[2] = 'pears'
print(fruits)

#A tuple is used for coordinates and is static
position = (2, 'hello')
color = (255, 255, 255)
print(type(color))

"""Iteration by Item"""

fruits = ['apples', 'bananas', 'pears', 3, 9, 2.3]

for fruit in fruits:
  if fruit == 'pears':
    print(fruit)
  else:
    print("not pears")

print()

for i in range(len(fruits)):
  if fruits[i] == "pears":
    print(fruits[i])
  else:
    print("not a pear")

"""String Methods"""

text = input("Enter a sentence: ")
print(text.strip()) #strip() removes white spaces before and after text
print(len(text)) #len returns length of a string
print(text.lower()) #converts text to lowercase
print(text.upper()) #converts everything to upper case
print(text.split('.')) #split() creates a list from a string
print(text.split()) #split() will deliminate space by default

"""Slice Operator"""

fruits = ['apples', 'pear', 'banana']
text = 'I am learning Python'

print(text[0:6]) #start:stop:step
print(text[:5]) #starts at beginning
print(text[2:]) #stops at end of string

print(text[::2]) #step through by 2
print(text[1::3])

print(fruits[1:])

#insert an element into the list
fruits[0:0] = 'O' #insert at beginning
fruits[2:2] = 'b'
fruits[5:5] = 'a' #insert at the end
print(fruits)

""".count() and .find()"""

string = 'hello'
print(string.find("l"))
print(string.count("l"))

user_input = input("Enter a string: ")
if user_input.count("_") > 0:
  print("Not good")
else:
  print("Good")

"""Introduction to Modular Programming"""

import math
#import myModule

print(math.pi)
print(math.degrees(math.pi))
print(math.radians(math.pi))
print(math.radians(60))

"""Optional Parameters"""

#etting the parameter to a value is called optional parameter
def func(x=2):
  return x**2

call = func()
print(call)

op = func(5)
print(op)

#print a word multiple times
def freq(word, freq):
  print(word*freq)

f = freq('Adwith', 3)
print(f)

#print a word using optional parameters
def freq2(word, freq=1, add=5):
  print(word * (freq+add))

f2 = freq2('hello')
f3 = freq2('hello', 2, 5)

"""Try and Except"""

text = input('Username: ')
 try:
  number = int(text)
  print(number)

except:
  print("Invalid Username")

"""Global vs Local Variables"""

var = 9
loop = True

def func(x):
  global loop 

  loop = 7

  if x == 5:
    return newVar

def otherFunc():
  newVar = 5

func(2)
print(loop)

"""Classes and Objects"""

x = 'string'
y = 23

print(type(y))
print(type(x))

class number():
  def __init__(self, num):
    self.var = num
  
  def display(self, x):
    print(x)

num = number(23)
num.display(num.var)

"""Static and Class Methods"""

class person(object):
  population = 50
  def __init__(self, name, age):
    self.name = name
    self.age = age 
  
  @classmethod
  def getPopulation(cls):
    return cls.population
  
  @staticmethod
  def isAdult(age):
    return age >= 18

  def display(self):
    print(self.name, "is ", self.age, " years old")

newPerson = person('Adwith', 22)

print(person.getPopulation())
print(person.isAdult(20))

"""Map() Function"""

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
  return x**x

#map function applies a function to every value in list and then returns the new values in a new list
print(list(map(func, li)))

"""Filter() Function"""

def add7(x):
  return x+7

def isOdd(x):
  return x%2 != 0

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#li2 = list(filter(isOdd, li))
li3 = list(map(add7, filter(isOdd, li)))

print(li3)

"""Lambda Tutorial"""

#lambda helps clean functions
#lambda is used only when you have one return statement

func2 = lambda x: x+5/4
print(func2(9))

#You can also define a function within a function
def func(x):
  func3 = lambda x: x+3
  return func3(x) + 85

print(func(2))

#now using with map and filter functions
a = [1,2,3,4,5,6,7,8,9,10]
newList = list(map(lambda x: x*2,a))
print(newList)