#while loop = execute some code WHILE some condition remains true
"""
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")
"""
#-----------------------------------------------#

"""
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative!")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")
"""

"""
food = input("Enter the food you like: (q to quit)")

while not food == "q":
    print(f"Your favourite food is {food}")
    food = input("Enter the food you like: (q to quit)")

print("bye")
"""


#Enter a number 1 - 10 exercise
"""
nr = int(input("Enter a number 1 - 10:  "))

while nr < 1 or nr > 10:
    print(f"{nr} is invalid")
    nr = int(input("Enter a number 1 - 10:  "))

print(f"Your number is {nr}")
"""

#Now the classic one: 
#print 10 times hello world

count = 0

while count < 10:
    print(f"{count+1}.Hello world")
    count += 1
