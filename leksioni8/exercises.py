#Ushtrimi 1:
"""
Krijo një klasë `Libri` me atributet: 
`titulli`, `autori`, `nrFaqe`. 
Shto një metodë `pershkrim()` që kthen një 
string me informacionin e librit.
"""
"""
class Libri:

    def __init__(self, titulli, autori, nrFaqe):
        self.titulli = titulli
        self.autori = autori
        self.nrFaqe = nrFaqe

    def pershkrimi(self):
        return f"{self.titulli} | {self.autori} | {self.nrFaqe} faqe"
    
    def __str__(self):
        return f"{self.titulli} | {self.autori} | {self.nrFaqe} faqe"

l1 = Libri("48 rules of power", "Robert Greene", 480)
print(l1)
"""

#Ushrimi 2
"""
Krijo një klasë Makina me atributet 
marka, modeli, viti. 
Shto një metodë pershkrim() që kthen një 
string me të dhënat e makinës.
"""

#Ushtrimi 3
"""
Krijo nje klase me emrin “Banka” , klasa duhet te kete atributet
dhe metodat meposhtme: 
--Atributet: 
    -->account_number, balance 
--Metodat:
    printBalance(),  withdraw(amount) , deposit(amount) 
"""
"""
class Banka:
    
    def __init__(self, balance):
        self.account_number = "123-456-789-1000"
        self.balance = balance

    def printBalance(self):
        print("printing balance...")
        print(f"Card Number:{self.account_number} | Balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Shuma tejkalon balancen tuaj!")
        else:
            self.balance -= amount
            print(f"${amount} u terhoqen me suskes")

    def deposit(self, amount):
        self.balance += amount
        print(f"Depozitimi i ${amount}, u krye me sukses.")
b1 = Banka(1000)
b1.printBalance()
b1.withdraw(500)
b1.deposit(700)
"""


#Ushtrimi 4:
"""
Ju po ndërtoni sistemin e një klinikë fizioterapie.

--> Krijoni një klasë të quajtur Patient.

--> Metoda __init__ duhet të pranojë name, injury, 
    dhe prescribed_sessions.

--> Shtoni një atribut të paracaktuar të quajtur sessions_completed 
    dhe vendosni vlerën e tij në 0.

--> -Krijoni një metodë të quajtur attend_session().
    -Sa herë që kjo metodë thirret, ajo duhet t'i 
     shtojë 1 vlerës sessions_completed dhe të printojë: 
     një mesazh si: "Alex just completed a session for their back pain. 
     (1/5 sessions done).
"""



#Ushtrimi 5: Digital dashboard for a motorcycle
"""
Ju po programoni një dashboard për një motoçikletë.

--> Krijoni një klasë të quajtur Motorcycle.

--> Në metodën __init__, kërkoni një brand dhe një model 
--> Jepini një atribut fuel_level që fillon nga 100 
    (që përfaqëson përqindjen) dhe një atribut mileage 
    që fillon nga 0.

--> Krijoni një metodë drive(km). Çdo 1 km e udhëtuar redukton karburantin me 1%. 
    Kjo metodë duhet të përditësojë vlerën e mileage 
    dhe të zvogëlojë vlerën e fuel_level.

--> Bonus: Sigurohuni që motoçikleta nuk mund të udhëtojë nëse Kilometrat 
    (km) e kërkuara janë më të mëdha se fuel_level aktual. 

"""

#Ushtrimi 6: E-Commerce shopping cart
"""
Ju po ndërtoni një shopping cart (checkout) 
për një dyqan online.

--> Krijoni një klasë Product. 
    -->Metoda __init__ duhet të kërkojë (name) dhe (price).

--> Krijoni një klasë ShoppingCart. 
    Metoda __init__ nuk merr asnjë parametër, 
    por duhet të krijojë një atribut të quajtur (items) 
    dhe ta përcaktojë atë si një listë boshe [].

--> Shtoni një metodë add_product(product) tek klasa ShoppingCart
    e cila shton një objekt të tipit Product në listën items.

--> Shtoni një metodë calculate_total(). 
    Ajo duhet të kalojë me loop nëpër të gjitha produktet në listën items,
    të mbledhë çmimet e tyre dhe të kthejë shumën totale.
Krijoni tre produkte të ndryshme, shtojini ato në një shportë blerjesh 
dhe printoni totalin përfundimtar.
"""
#Product
class Product:
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}: ${self.price}"
laptop = Product("Laptop", 700)
print(laptop)

mouse = Product("Mouse", 5)

class ShoppingCart:
    def __init__(self):
        self.items = []
    #add_product(laptop)
    def add_product(self, product:Product):
        self.items.append(product)
    #-->e cila shton një objekt të tipit Product në listën items.

    #calculate_total()
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price    

        return f"Total = ${total}"
    #-->Printon totalin e produkteve per tu paguar

cart = ShoppingCart()
cart.add_product(laptop)
cart.add_product(mouse)
print(cart.calculate_total())

