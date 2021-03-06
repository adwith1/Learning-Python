# -*- coding: utf-8 -*-
"""Practice1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10a6Kd_uRhftvoyp8hIdCYZ5YGqAP3-u3
"""

from math import *

"""Getting Started: Hello World!"""

print("Hello World")

"""Make a shape using Print"""

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

"""How to use Variables"""

character_name = "Tony"
character_age = 20
is_male = True

print("There once was a man named " + character_name + ", ")
print("He was " + str(character_age) + " years old.")
print("He really liked the name " + character_name)
print("but he didn't like being " + str(character_age))

"""Strings"""

college = "Arizona State University"
print(college)
print(college.lower())
print(college.upper())
print(college.isupper())

#conver to upper case and then check if upper case
print(college.upper().isupper())

#check the length of the string
print(len(college))

#get a character in a string
print(college[0])
print(college[3])

#print the index of a character
print(college.index("State"))

#replace part of string
print(college.replace("Arizona", "Oregon"))

"""Numbers"""

print(4.123)

pi = 3.14
print("The pi constant value is: " + str(pi))
print(pow(2,2))
print(round(3.14))

x = -2
print(abs(x))

print(floor(3.7))
print(ceil(3.7))
print(sqrt(4))

"""Get Input from User"""

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "!")
print("You are " + age + " years old")

"""Basic Calculator"""

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = float(num1) + float(num2)
print("The sum is: " + str(sum))

"""Mad Libs Game"""

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

"""Lists"""

#A list is a data structure in python that is mutable 
#or changeable, ordered sequence of elements.
#Each element inside the list is called an item

#Elements in lists can be of any type

friends = ["Berlin", "Tamille", "Harshita", "Aaron"]
example = ["Adwith", 1, True]

#print out entire list
print(friends)

#print first element in list
print("The first element in the list is: " + friends[0])

#print second element in list
print("The second element in the list is: " + friends[1])

#print third element in list
print("The third element in the list is: " + friends[2])

#Another way to print out the last value of the list is [-1]
print("The last element in the list is: " + friends[-1])

#Select the last two elements of the list
print(friends[1:])

#Specify the range
print(friends[1:3])

#modify an element of the list
friends[3] = 'Sebastian'
print(friends)

"""List Functions"""

my_numbers = [1, 2, 3, 4, 5]
friends2 = ["Harshita", "Harshita", "Berlin", "Tamille", "Aaron"]

#extend function appends a list to another list
friends2.extend(my_numbers)
print(friends2)

#append another item onto the end of the list
friends2.append(6)
print(friends2)

#insert an item into the list using insert function
#first parameter is index, second is value
friends2.insert(4, "Sebastian")
print(friends2)

#remove an item from the list, pass in the value as parameter
friends2.remove(6)
print(friends2)

#pop an item of the list using the pop function
friends2.pop()
print(friends2)

#Check if a certain value is in the list
print(friends2.index("Berlin"))

#Look for duplicates in the list
print(friends2.count("Harshita"))

#Sort the list, sorts in alphabetical order
friends.sort()
print(friends)

#reverse the items in a list
my_numbers.reverse()
print(my_numbers)

#Create another list and make it as a copy
friends3 = friends2.copy()
print(friends3)

#reset the list
friends2.clear()
print(friends2)

"""Tuples"""

#Tuples are a collection of objects that are ordered and
#are immutable. They are sequences just like lists, but are
#different from lists since tuples can not be changed.

coordinates = (4, 5)
print(coordinates)

#print out each element in the tuple
print(coordinates[0])
print(coordinates[1])

"""Functions"""

#create a function that says hi
def greeting(name, age):
  print("Hello " + name)
  print("You are " + age + " years old.")

greeting("Adwith", "22")
greeting("Miras", "29")

"""Return Statement"""

def cube(data):
  return data*data*data

result = cube(2)
print(result)

"""If Statements"""

is_male = True
is_tall = True

if is_male and is_tall:
  print("You are a male and tall")

elif is_male and not (is_tall):
  print("You are a short male")  

elif not(is_male) and is_tall:
  print("You are not male and are tall")

else:
  print("You are not a male and not tall")

"""If Statements and Comparisons"""

def max_num(x, y, z):
  if x >= y and x >= z:
    return x
  elif y >= x and y >= z:
    return y
  else:
    return z


print(max_num(1,71,5))

"""Improved Calculator"""

input1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
input2 = float(input("Enter a number: "))

if op == "+":
  print(input1 + input2)
elif op == "-":
  print(input1 - input2)
elif op == "*":
  print(input1 * input2)
elif op == "/":
  print(input1 / input2)
else:
  print("Invalid operator.")

"""Dictionaries"""

#Dictionaries are an unordered collection of items that have
#key/value pairs. Dictionaries are optimized to retrieve
#values when the key is known.

#Convert abbrivieated form of month name to full name
monthConversion = {
    #Key:Value
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

#Access a value in the Dictionary using the key as index
print(monthConversion["Feb"])
print(monthConversion["Jun"])

#Use get function to retrieve value in dictionary
print(monthConversion.get("Dec"))

#Have a default value if you can not find a value with key
print(monthConversion.get("snf", "Not a valid key"))

"""While Loop"""

x = 1
while x <= 10:
  print(x)
  x += 1

print("Done with loop")

"""Guessing Game"""

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("You have 3 tries to guess the word.")
while guess != secret_word and not (out_of_guesses):
  if guess_count < guess_limit:
    guess = input("Enter guess: ")
    guess_count += 1

  else:
    out_of_guesses = True
    
    
if out_of_guesses:
  print("Out of Guesses, you lose!")

else:
  print("You win!")

"""For Loop"""

college_friends = ["Harshita", "Berlin", "Tamille"]
for friend in college_friends:
  print(friend)

for index in range(len(friends)):
  print(friends[index])  

#print every number in a range
for index in range(10):
  print(index)

"""Exponent Function"""

def raise_to_power(base_num, pow_num):
  result = 1
  for index in range(pow_num):
    result = result * base_num
  return result

print(raise_to_power(3, 3))

"""2D Lists and Nested Loops"""

number_grid = [
               #4 rows, 3 columns
               [1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [0]
]

#print the first element in the 2D list
print(number_grid[2][0])
print()

for row in number_grid:
  for column in row:
    print(column)

"""Translator"""

#Created language rules:
#vowels -> g
#-------------

#dog -> dgg
#cat -> cgt

def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter.lower() in "aeiou":
      if letter.isupper():
       translation = translation + "G"
      else:
        translation = translation + "g"
    else:
      translation += letter 
  return translation

user_input = input("Enter a phrase: ")
print(translate(user_input))

"""Try Except"""

try:
  value = 10/0
  number = int(input("Enter a number: "))
  print(number)

except ZeroDivisionError as err:
  print(err)

except ValueError:
  print("Invalid input.")

"""Classes and Objects"""

#A class is a blue print from which the objects are created.
#A class represents a set of properties or methods that are
#common to all objects of one type.
#Objects are basic structures that represent entities with a 
#state, behaviour, and identity. Objects are instances of a class.
#USE BOTH TO CREATE YOUR OWN DATA TYPE.

class student:
  
  def __init__(self, name, major, gpa, is_on_probation):
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation

student1 = student("Harshita", "Biodmedical Science", 3.1, False) 
student2 = student("Berlin", "Computer Science", 4.0, True)

print(student1.name)
print(student1.gpa)

"""Multiple Choice Quiz"""

question_prompt = [
                   "Who is Iron Man?\n(a) Tony Stark\n(b) Adwith Malpe\n(c) Nobody\n\n",
                   "Which is the best pizza place?\n(a) Pizza Hut\n(b) Dominoes\n(c) Papa Johns\n\n",
                   "Which is the best car company?\n(a) Audi\n(b) Mercedes\n(c) BMW\n\n" 
]

class question:
  def __init__(self, prompt, answer):
    self.prompt = prompt
    self.answer = answer

questions = [
             question(question_prompt[0], "b"),
             question(question_prompt[1], "a"),
             question(question_prompt[2], "a")
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

