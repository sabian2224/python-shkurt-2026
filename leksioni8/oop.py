#---------------------Python OOP---------------------#
#Çfarë është OOP?
#--> Object Oriented Programming
#Python është gjuhë object-oriented, 
#të lejon të strukturosh kodin tënd duke përdorur classes dhe objects

#--Avantazhet e OOP--
"""
--.Ofron një strukturë të qartë për programet.

--.E bën kodin më të lehtë për t'u mirëmbajtur, ripërdorur dhe për t'i bërë debug.

--.Ndihmon ta mbani kodin tuaj DRY (Don't Repeat Yourself).

"""

#Classes & Objects
"""
Një class përcakton se si duhet të duket një object, 
dhe një object krijohet duke u bazuar tek ajo class. 
Për shembull:
| -------------------------------------------------- |
| Class: Frut   --> Objects: [molle, mango, dardhe]  |
| Class: Makine --> Objects: [volvo, audi, toyota]   |
| -------------------------------------------------- |

"""

#Krijimi i nje klase:
class Makina:
    
    #constructor ose initializer
    def __init__(self, marka, modeli):
        self.marka = marka
        self.modeli = modeli

m1 = Makina("Audi", "a4")
print(m1.marka)
print(m1.modeli)


#Class Properties
"""
Properties janë variablat që i përkasin një klase.
Ato ruajnë të dhëna për çdo object të krijuar nga ajo klas.

"""


#Krijimi i nje objekti:


#Disa objekte
"""
p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
print(p1.name)
print(p2.name)
print(p3.name)
print(p4.name)

"""

#Python __init__() Method
"""
Të gjitha klasat kanë një built-in method të quajtur __init__(), 
e cila ekzekutohet gjithmonë kur class-a inicializohet.

--> Constructor
--> Initializer
--> Special method
    -->Metoda te cilat mund ti bejme override

--> Perdorimi i __init__() e ben me telehte 
    inicializimin e objekteve me vlera fillestare.
"""


#Parametri self
"""
--> Parametri self është një referencë për instancën aktuale të klasës.
--> Në Java, kur thërrisni një method në një object (p.sh. c.method()), 
    compiler-i e di vetë që çdo variabel instance i përket atij objekti 
    specifik.

--> Java: this (Implicit) --(reserved keyword).
--> Python: self (Explicit) -- Jo (reserved keyword) 
    por duhet të jetë gjithmonë parametri i parë i constructor-it.
"""



#Shembull: 
""" 
--> Krijoni një class me emrin Person.
--> Shtoni një method __init__ që merr name dhe age si parameters.
--> Shtoni një method të quajtur greet që printon "Hello, my name is " 
    të ndjekur nga emri (name).
--> Krijoni një object p1 të kësaj class-e me name "John" dhe age 36.
--> Thërrisni method-ën greet tek p1.

"""

#Shembull
"""
Krijo një klasë Makina me atributet 
marka, modeli, viti. 
Shto një metodë pershkrim() që kthen një 
string me të dhënat e makinës.
"""

