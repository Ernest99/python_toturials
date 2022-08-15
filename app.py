from audioop import add
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

# def greetings_function(name, age):
#   print("Hello " + name + " . You are " + str(age) + " years old.")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# greetings_function(name, age)


# def add_numbers(num_1, num_2):
#   return num_1 + num_2
# num_1 = int(input("Enter your first number: "))
# num_2 = int(input("Enter your second number: "))
# print(add_numbers(num_1, num_2))

 

# value = input("Enter your sentences: ")
# print(len(value))

# if len(value) < 10:
#   print(value, " is less than ten")
# else:
#   print(value, " is more than ten")

my_dict = {
  'name': 'max',
  'student': True,
  'age': 20

}
print(my_dict["name"])

i = 1

while i < 10:
  print(i * '*')
  i += 1



my_list = list(('so','go','lo','he','we'))
for list in my_list:
  print(list)

my_detail = {
  'name': 'Max',
  'age': 20,
  'sex': 'Male'
}

for detail in my_detail:
  print(detail)



#basic calculator

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operator = input("Enter operator(+, -, *, /, %): ")

if operator == '+':
  print(num_1 + num_2)
elif operator == '-':
  print(num_1 - num_2)
elif operator == '/':
  print(num_1 / num_2)
elif operator == '%':
  print(num_1 % num_2)
elif operator == '*':
  print(num_1 * num_2)

else:
  print("operator is invalid: ")
