from math import *


print('Hello world')
name = 'Tim'
age = 12
# i used the python casting method for the 'age'[Casting is changing the data type of a specific data]
txt = ("Hello {}, and i am {} years old")# python format method[{} then the format()]
print(txt.format(name,age))
#this is a python toturial for beginners
Name = "Ernest"
print(Name.lower().islower())
print(len(Name))

print(name.replace('T','K'))
print(type(Name))
print(type(age))

x = 'awesome'

def myFunc():
  global  x
  x = 'great'
  print('Python is ', x)

myFunc()

print('python is ' + x)

print(sqrt(100))

# name_detail = input('Enter your name: ')
# print(name_detail)

# sentence = input('Enter your sentence: ')
# print(sentence)
# word_1 = input('Enter the word to replace: ')
# word_2 = input('Enter the word to replace it with: ')
# result = (sentence.replace(word_1,word_2))
# print(result)
# for results in result:
#     print(results)

countries = ["United kingdom","Ghana","Nigeria","Australia","Kenya","Japan"]
countries[0] = "United State"

length = len(countries)
print(length)

print(countries)
print(countries[-1])

fruit = list(("Mango","Banana","Orange","Pear","Strawberry","Apple"))
fruit_2 = fruit.copy()
print(fruit_2)

countries.extend(fruit)
print(len(countries))
# countries.append('France')
# print(countries)
# cities = ["Accra","Abuja","Rio","Cape Vade","New York"]

# countries.extend(cities)

# print(type(countries))

#functions

def greetings_function(name, age):
  print("Hello " + name + " . You are " + str(age) + " years old.")
name = input("Enter your name: ")
age = input("Enter your age: ")
greetings_function(name, age)

