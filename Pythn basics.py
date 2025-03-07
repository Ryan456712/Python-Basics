#Pythin Basics

#Print function
print("Hello World")

#Variables

#String(letters)
name ="Jhon"
print(name)

#Interger(numbers)
age = 25
print(age)

#Float(decimals)
Height = 1.75
print(Height)

#Boolean(True/False)
employed = True
print(employed)

#lists
Fruits = {"apple","banana","orange"}
print(Fruits)

#Dictionary 
person1 = {"name":"Jhon","age": 25,"Height":1.75, "employed": True}
print(person1)

#Key Value pairs
print(person1["name"])
print(person1["employed"])
print(person1["age"])
print(person1["Height"])
#Array(list)
intergers= {12,34,76,42}
print(intergers)

Floats = {-12,1.78,-78,45.5}
print(Floats)

#math operations

Num1 = 5
Num2 = 445

#Addition

print(Num1 + Num2)

#subtraction

print(Num1 - Num2)

#Multiplication

print(Num1 * Num2)

#Division

print(Num1 / Num2)


#User input

number1 = input("Enter 1st number: ")
print(number1)

print('the number you jsut enterd was = ', number1)

#conditionals

#input function is expecting am an int
age = int(input("Enter your age: "))
#if age is less than 13 then print you are a kid
#if age is 13 to 17, then print you are a teenager
#if age is 18 to 60, then you are an adult
#if anything else(more than 60, you are a senior)

if age < 13:
    print("you are a kid")
elif age >= 13 and age <= 17:
    print("you are a teenager")
elif age >= 18 and age <= 60:
    print("you are not an adult")
else:
    print("you are not a kid")

#For loops

for i in range(0,10):
    print(i)

#for loop that print my name 10 times
    
for i in range(0,16):
    print("Ryan")

#for loop that prints the numbers 1 to 10
    
for i in range(1,16):
    print(i)

#for loop that prient random unmbers from 1 to 10
    
import random
for i in range(0,10):
    print(random.randint(1,10))

#for loop that prints the numbers 1 to 10 in reverse order
    
for i in range(10,0,-1):
    print(i)

#While loops
boolean = input("Enter True or False: ")
    
while boolean == "True":
    print("You entered True")
    boolean = input("Enter True or False: ")
else:
    print("You entered False")

#while loop that prints ("tea,coffee") 10 times
    
i = 0
while i < 10:
    print("tea,coffee")
    i += 1
else:
    print("Loop has ended")

#while loop for russian roulette
    
import random
bullet = random.randint(1,6)
i = 1
while i <= 6:
    print("Spinning the chamber")
    print("Pulling the trigger")
    if i == bullet:
        print("You are dead")
        break
    else:
        print("You are alive")
    i += 1
else:
    print("You are alive")

#while loop that prints the numbers 1 to 10
    
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("Loop has ended")

#Python functions
    
def say_hello():
    print("Hello")

say_hello()

def say_hello(name):
    print("Hello", name)

say_hello("Ryan")

#Python functions math
    
def add(num1, num2):
    return num1 + num2

print(add(7, 6))
print(add(32, 423))
print(add(45, 67))

def subtract(num1, num2):
    return num1 - num2

print(subtract(7, 6))
print(subtract(32, 423))
print(subtract(45, 67))

def multiply(num1, num2):
    return num1 * num2

print(multiply(7, 6))
print(multiply(32, 423))
print(multiply(45, 67))

def divide(num1, num2):
    return num1 / num2

print(divide(7, 6))
print(divide(32, 423))
print(divide(45, 67))

#Python functions stringS

str1 = "Hello"
str2 = "World"
extended_str = str1 + " " + str2
print(extended_str)

def add_strings(str1, str2):
    return str1 + " " + str2

print(add_strings("Hello", "World"))
print(add_strings("Ryan", "Smith"))
print(add_strings("Python", "Programming"))

#lists and loops with strings

fruits = ["apple","banana","cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

list_length = len(fruits)
print("length of fruits array is = ", list_length)

for i in range(0, list_length):
    print(fruits[i])

for fruit in fruits:
    print(fruit)

#lists and loops with numbers
    
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])

list_length = len(numbers)
print("length of numbers array is = ", list_length)

for i in range(0, list_length):
    print(numbers[i])

for number in numbers:
    print(number)

#lists and loops with mixed data types
    
mixed = ["cherry", 6, 45.7, True]
print(mixed)
print(mixed[0])
print(mixed[1])
print(mixed[2])

list_length = len(mixed)
print("length of mixed array is = ", list_length)

for i in range(0, list_length):
    print(mixed[i])

for item in mixed:
    print(item)

    


