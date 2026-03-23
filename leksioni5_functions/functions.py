#Functions in python: Leksioni 5
"""
--* Një funksion është një bllok kodi që ekzekutohet vetëm kur thirret.

--* Si rezultat, një funksion mund të kthejë të dhëna.

--* Një funksion ndihmon në shmangien e përsëritjes së kodit.
"""


#-----------Part 1: Prezantimi i funksioneve---------------
"""
   Në Python, një funksion përcaktohet duke përdorur fjalën kyçe "def",
   e ndjekur nga një emër funksioni dhe kllapa:

    **    def my_function():
            print("Hello from a function")
    **
"""
#--Shembull: Printo emrin e perdoruesit
"""
name = input("Emri: ")#Global Variable
def print_users_name(name):
    print(f"Pershendetje {name}")
    print("Sot do te mesojme funksionet ne python")
    print("Siguro laptopin dhe degjo mesimin")

#Thirrja e funksionit:
print_users_name(name)
"""


#--Shembull: Siperfaqja e drejtkendeshit:
            #a, b jane parametrat e funksionit
def rec_area (a, b):#<---- Functions header
    #local scope
    area_calculated = a * b# <---- Functions Body
    print(area_calculated) # <---- Functions Body
    #Local Variables

#Thirrja e funksionit:
"""
rec_area(5, 10) #5 dhe 10 jane argumente

"""

#--Shembull:
#Krijo nje funksion i cili mer si argument emrin dhe moshen tuaj.
#Printon: Ckemi {emri}, ti je {mosha} vjec, Gezuar Ditelindjen!
"""
emri = "Sabian"
mosha = 24

def happy_bday(emri, mosha):
    print(f"Ckemi {emri}, ti je {mosha} vec. Gezuar ditelindjen")


#Thirrja e funksionit
happy_bday(emri, mosha)
"""


#--Shembull: Shfaqja e fatures
#Krijo nje funksion i cili mer si argument emrin dhe shumen e fatures ne $
#Funksioni printon: Pershdentje {emri}!
#                   Fatura juaj: Emri: {emri}, Shuma per tu paguar: {shuma}
"""
emri = "Sabian"
shuma = 1000

def printo_faturen(emri, shuma):
    print(f"Pershendetje {emri}! \nFatura juaj: Emri: {emri}, shuma per tu paguar: ${shuma}")

printo_faturen(emri, shuma)
"""
#====================Part 1 End====================#


#----------Part 2: Return Statement------------------
# return = mbyll funksionin dhe kthe dicka mbrapsht

#--Shembulli 1: Shuma
"""
def mblidh (x, y):
    return x + y

print(mblidh(5, 10))
"""

#Shembulli 2: Zbritje

#Shembulli 3: Shumezim 

#Shembulli 4: Pjestim


#Shembulli 5:
#Krijo nje funksion qe mer si argument emrin dhe mbiemrin tuaj
#Funksioni kthen mbrapsht emrin dhe mbiemrin tend te kapitalizuar:
#Emri Mbiemri
#nidhme: perdor capitalize() function
"""
emri = "sabian"
mbiemri = "zhupa"

def printo_emrin_capitalize(emri, mbiemri):
    full_name = emri.capitalize() +" " +mbiemri.capitalize()
    return full_name

print(printo_emrin_capitalize(emri, mbiemri))

"""



#test:
"""
def printHello():
    print("Helloooo")

results = printHello()
print(results)
"""

#====================Part 2 End====================#


#--------------------Ushtrime Praktike-------------------#

#Ushtrimi 1: Mesatarja e notave (pa sum())
"""

Krijo funksionin average(grades) që:

--> merr listë me nota (0–100)

--> llogarit mesataren me for

--> nëse lista është bosh → kthen None

"""
"""
grades = []
add_more = True
counter = 0

while add_more:
    check = input("Vazhdoni me shtimin e notes (y/n)")
    if check == "y":
        counter +=1
        grades.append(int(input("Grade " +str(counter) +": ")))
    else:
        add_more = False

print(grades)

def average(grades):
    if len(grades) == 0:
        return None
    shuma = 0
    for x in grades:
        shuma += x
    avg = shuma / len(grades)
    return avg

print(average(grades))
"""

#Ushtrimi 2: Gjej maksimumin (pa max())
"""

Krijo funksionin find_max(nums) që:

--> merr listë numrash

--> kthen numrin më të madh

--> nëse lista është bosh → kthen None

"""

#Funksioni per marjen e inputit nga useri
def list_initialization():
    lista = []
    add_more = True
    counter = 0

    while add_more:
        check = input("Vazhdoni me shtimin e numrit (y/n)")
        if check == "y":
            counter +=1
            lista.append(int(input("Numri " +str(counter) +": ")))
        else:
            add_more = False

    return lista


def find_max(nums):
    max_num = nums[0]
    for x in nums:
        if max_num < x:
            max_num = x

    return max_num


#Inicializojme listen
nums = list_initialization()
print(f"Vlera maksimale = {find_max(nums)}")







#Ushtrimi 3:  Filtro numrat mbi limit
"""

Filtro numrat mbi limit

--> Krijo funksionin greater_than(nums, limit) që:

--> kthen listë të re vetëm me numrat > limit

--> mos përdor filter()

"""




#Ushtrimi 4: Calculator me operator
"""

Krijo funksionin calc(a, b, op) që:

--> op mund të jetë: "+" , "-" , "*" , "/"

--> kthen rezultatin

--> nëse op sështë valid → kthen "Invalid operator"

--> nëse / dhe b == 0 → kthen "Cannot divide by zero"

"""

#Ushtrimi 5: Mini Bank System

"""
Ndërto një program “Mini Bank System” që:

--> Ka një balance fillestar (p.sh. 1000)

--> Ka një card_number fiks (p.sh. "1234-5678-9101")

--> Ka funksione:

    *--> deposit(balance, amount) → shton shumën dhe kthen balancen e re

    *--> withdraw(balance, amount) → heq shumën nëse ka mjaftueshëm, përndryshe jep mesazh dhe kthen balance pa ndryshim

    *--> check_balance(card_number, balance) → shfaq kartën dhe balancën
    

Shfaq menunë: depozitim (d), tërheqje (t), shiko balancën (s)

Programi duhet te perseritet derisa user-i të shkruajë "n"

======== Mini Bank System ========
Miresevini ne Mini Bank System!

-------------------------------
Card Number: 1234-5678-9101
Your balance: $1000

Cilin nga veprimet deshironi te kryeni?
Depozitim (d)
Terheqje (t)
Shiko balancen (s)
Zgjedhja:

"""
