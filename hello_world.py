# -*- coding: utf-8 -*-
"""Hello world

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P1pReKFEVZRkkl3Itby2v0j9U2IxyDQJ
"""

print("Hello World")  #this is basics of python to print hello world

name = "Simran"
age = 23
Id = 2000
print("My name is", name, "and I'm", age, "years old", "with id",Id)
#here print is used to print the output containing the variables

myfriend="Sukh"
print("My best friend is",myfriend,"\nShe is very kind and smart")
#here \n is used to print the output in new line

print("She is my \"Best friend forever\"")
#here \" is used to print the output in double quotes

a = 'She said,"I need to study hard"'
print(a)
#here print is used to print the string that conatin both single and double quotes

A1 = "1"
A2 = "2"
print("Concat two digits:",A1 + A2)
#here print is concatinating the strings

a = 10
b = 15
print("Adding two  numbers:",a + b)
#here print is adding the numbers

State="Punjab"
print(f"I am {name}, I am {age} years old, I am from {State}")
#here f is used to print the string with variables

print('''My friend is  also of same  age
She is from Haryana''')
print("""She is  also from same college""")
#here triple single or double quotes are used to print the output in multiple lines

print("My nickname is",name[0:4])
#here [0:4] is used to print the output from 0 to 4 index

for character in State:
  print(character)
#here for loop is used to print the output of each character of the string

Friends="Viewers"
print("So this the end of the program",Friends,"Thanks for watching")