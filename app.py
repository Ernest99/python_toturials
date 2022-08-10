from math import *


print('Hello world')
name = 'Tim'
age = 12
# i used the python casting method for the 'age'[Casting is changing the data type of a specific data]
print(" Hello " + name + ",\n I am " + str(age) + ' years old')
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

sentence = input('Enter your sentence: ')
print(sentence)
word_1 = input('Enter the word to replace: ')
word_2 = input('Enter the word to replace it with: ')
result = (sentence.replace(word_1,word_2))
print(result)
# for results in result:
#     print(results)