#=======Dictionaries in Python=======#

#Dictionaries përdoren për të ruajtur vlerat e të dhënave në çifte key:value.
#Koleksion i cili:
# 1.është i renditur
# 2.i ndryshueshëm
# 3.nuk lejon dublikate.

#--> Key: etiketa e cila perdoret per te aksesuar vleren

#Krijo dhe printo një dictionary:



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}

#print(len(thisdict))
#print(type(thisdict))


#========-- 1. Aksesimi i artikujve --========

#Aksesimi i artikujve
"""
print(thisdict["brand"])
print(thisdict.items())

x = thisdict["brand"]
print(x)
print(thisdict.items())

x = thisdict.get("model")
print(x)
"""

#Aksesimi i Keys
"""
x = thisdict.keys()
print(x)
"""

#Aksesimi i Values
"""
x = thisdict.values()
print(x)
"""
"""
#Modifikimi i values:

thisdict["year"] = 2020
thisdict["model"] = "Range"
print(thisdict["year"])
print(thisdict["model"])

#Shto nje key & value pair

thisdict["color"] = "red"
print(thisdict.keys())
print(thisdict.values())
thisdict["state"] = "CA"
print(thisdict["state"])

studentet = {
}

for x in range(1, 5):
    studentet[f"studenti{x}"] = input("Emri i studentit")
"""


#1.1:Updating Dictionaries
#Metoda update() do të përditësojë dictionary-n me elementët nga argumenti i dhënë.
"""
thisdict.update({"year": 2020})
"""

#1.2:Adding Items
"""
thisdict["color"] = "red"
print(thisdict)
"""

#1.3:Remove Dictionary Items
#Metoda pop() heq artikullin me emrin e çelësit të specifikuar:
"""
thisdict.pop("model")
print(thisdict)
"""

#Fjala kyçe del heq artikullin me emrin e çelësit të specifikuar:
"""
del thisdict["model"]
print(thisdict)
"""

#Fjala kyçe del mund ta fshijë dictionary-n plotësisht:
"""
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

"""

#Metoda clear() zbraz dictionary-n:
"""
thisdict.clear()
print(thisdict)
"""


#1.4: Loop Dictionaries
#Mund të bëni loop në një dictionary duke përdorur një cikël for.

"""
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
"""


#Ju gjithashtu mund të përdorni metodën values() për të kthyer vlerat e një dictionary:
"""
for x in thisdict.values():
  print(x)

"""

#Mund të përdorni metodën keys() për të kthyer çelësat e një fjalori:
"""
for x in thisdict.keys():
  print(x)

"""

#Kaloni në ciklin midis çelësave dhe vlerave, duke përdorur metodën items():
"""
for x, y in thisdict.items():
  print(x, y)
"""

#1.5: Copy a Dictionary
#Nuk mund të kopjosh një dictionary thjesht duke shkruar dict2 = dict1, 
# sepse: dict2 do të jetë vetëm një referencë për dict1,
"""
mydict = thisdict.copy()
print(mydict)

"""


#1.6: Nested Dictionaries
"""
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
"""



#Access Items in Nested Dictionaries
#Për të aksesuar artikujt nga një fjalor nested, 
# përdorni emrin e dictionaries, duke filluar me fjalorin e jashtëm: 
"""
print(myfamily["child2"]["name"])

"""

#Loop Through Nested Dictionaries
"""
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

"""

"""
Ushtrim: Përdorimi i Dictionary me Loop

*Krijo një dictionary që përmban emrat e studentëve dhe moshën e tyre.

Shembull:

students = {
    "Anna": 22,
    "John": 19
}
Detyra:

Përdor një loop (for) për të kaluar mbi dictionary dhe printo rezultatin në këtë format:

Anna is 22 years old
John is 19 years old

Pra, programi duhet të lexojë automatikisht emrin dhe moshën nga dictionary, jo t’i shkruajë manualisht.
"""

students = {
    "Anna": 22,
    "John": 19
}

for student, age in students.items():
    print(f"{student} is {age} years old")




