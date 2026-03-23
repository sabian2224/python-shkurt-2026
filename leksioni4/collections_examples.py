#lists
#--> List = [] ordered and changeable. Duplicates OK
#fruits = ["apple", "orange", "coconut"]
"""
print(fruits[::1])#index operator

for fruit in fruits:
    print(fruit)
"""

#Methods to use with collection
#list the collection

#print(dir(fruits))

#print(len(fruits))

#if you wanna confirm apple is in fruits
#print("pineapple" in fruits)

#append() function add a new element
#fruits.append("pineapple")

#remove() method
#fruits.remove("pineapple")

#insert() method to insert it in a specific index
#fruits.insert(1, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()

#print(fruits.index("coconut"))
#print(fruits.count("coconut"))
#print(fruits)

#-------------Sets---------------

# Set = {} unordered and imutable, but Add/Remove OK. No duplicates

#fruits = {"apple", "orange", "banana", "coconut"}
#print(fruits)

#print(dir(fruits))
#print(help(fruits))
#len(fruits)

#We cannot change the elements
#fruits[0] = "pineapple"
#print("pineapple" in fruits)

#However we can add or remove elements
#fruits.remove("apple")
#fruits.pop() #random remove 
#fruits.clera() #Delete all

 
#------------------Tuples--------------------
#Tuple = () ordered and unchangeable. Duplicates OK. Faster
#Faster

fruits = ("apple", "orange", "banana", "coconut")
print(fruits.index("apple"))






