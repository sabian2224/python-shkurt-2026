"""
1. Student Grade Analyzer
Krijo një dictionary me notat e studentëve
Detyrat:
--> Printo të gjithë studentët bashkë me notat e tyre.
--> Gjej mesataren e notave.
--> Printo vetëm studentët që kanë kaluar, pra ata që kanë notë ≥ 70.
"""

"""
grades = {
    "Anna": 85,
    "John": 72,
    "Mike": 91,
    "Sara": 60
}

#1. Printo te gjithe studentet
for student, grade in grades.items():
    print(f"{student} : {grade}")


#2. Gjej mesataren e notave 
total = 0
for grade in grades.values():
    total += grade
avg = total / len(grades)
print(f"Mesatarja e notave: {avg}")

#3. Printo vetëm studentët që kanë kaluar
print("Studentet qe kan kaluar provimin: ")
for student, grade in grades.items():
    if grade >= 70:
        print(f"{student}")
"""

"""
2. Word Counter
*Kërko nga përdoruesi të shkruajë një fjali.

*Shembull input:
    `python is fun and python is powerful`

Detyra:
Ndërto një dictionary që numëron sa herë përsëritet çdo fjalë në fjali.

Output i pritur:
* `python : 2`
* `is : 2`
* `fun : 1`
* `and : 1`
* `powerful : 1`
"""

"""
sentence = input("Vendos nje fjali: ")
sentence = sentence.replace(",", "")
words = sentence.split()
print(words)
word_counter = {

}

for word in words:
    if word in word_counter:
        word_counter[word] +=1
    else:
        word_counter[word] = 1

print(word_counter)
"""

"""
========================----========================
3. Inventory Management System
*Krijoni një program për menaxhimin e stokut të një dyqani.

Programi duhet të përdorë këto funksione:

* `buy_product(inventory)` → përdoret për të blerë një produkt
* `show_inventory(inventory)` → shfaq të gjithë produktet dhe sasitë

Programi duhet të shfaqë këtë menu:

```
1 - Buy product
2 - Show inventory
3 - Exit
```

Kur përdoruesi zgjedh Buy product:

* kërkohet emri i produktit
* nëse produkti ekziston, sasia ulet me 1
* nëse sasia bëhet 0 → shfaqet “OUT OF STOCK”
* nëse produkti nuk ekziston → “Product not found”

Programi vazhdon derisa përdoruesi zgjedh Exit.

---
Shembull Output
```
1 - Buy product
2 - Show inventory
3 - Exit
Choose option: 1
Enter product: laptop
Laptop purchased successfully.

1 - Buy product
2 - Show inventory
3 - Exit

Choose option: 2
Inventory:
laptop : 3
mouse : 10
keyboard : 6
```
"""

inventory_items = {
    "laptop": 7,
    "airpods": 5,
    "cover": 20,
    "keyboard": 1
}

#1 - Buy product
#2 - Show inventory
#3 - Exit

#buy_product(inventory)
def buy_product(inventory_items): 
    print("------------------------")
    product = input("Enter product_")
    print("------------------------")
    if product in inventory_items:
        if inventory_items[product] == 0:
            print("------------------------")
            print("Product out of stock")
            print("------------------------")
        else:
            inventory_items[product] -= 1
            print("------------------------")
            print(f"{product} successfuly purchased.")
            print("------------------------")
          
    else:
        print("------------------------")
        print("Product not found")
        print("------------------------")

def show_inventory(inventory_items):
    print("------------------------")
    for product, stock in inventory_items.items():
        print(f"{product} : {stock}")
    print("------------------------")


run = True

#1.Buy Product
while run:
    print("(1) Buy product \n(2) Show Inventory \n(3) Exit")
    op = int(input("Choose option: ")) #op -> Option
    if op == 1:
        buy_product(inventory_items)

    #2. Show Invenotry
    elif op == 2:
        show_inventory(inventory_items)
    elif op == 3:
        print("------------------------")
        print("Inventory system closed")
        print("------------------------")
        run = False




            
"""
##4 Student Multiple Subjects

Structure:

students = {
    "Anna": {"math": 80, "english": 90},
    "John": {"math": 70, "english": 60},
    "Sara": {"math": 95, "english": 88}
}


Tasks:

* Print each student average
* Find best student overall
* Print highest math score.

"""


##6. Mini Banking Database
"""
Krijoni një program ATM në Python që përdor një dictionary
për të ruajtur llogaritë bankare.

Struktura e të dhënave:

accounts = {
 "1001": {"name": "Anna", "balance": 1200},
 "1002": {"name": "John", "balance": 500}
}

Programi duhet të shfaqë këtë menu:

```
1 Check balance
2 Deposit
3 Withdraw
4 Exit
```

Funksionet që duhet të krijohen

---> check_balance(accounts, card_number)** → shfaq balancën
---> deposit(accounts, card_number, amount)** → shton para në balancë
---> withdraw(accounts, card_number, amount)** → tërheq para nga balanca
---> main()** → menaxhon menunë dhe inputin e përdoruesit

### Rregullat

* Nuk mund të tërhiqen më shumë para se balanca
* Karta duhet të ekzistojë
* Dictionary duhet të përditësohet pas çdo veprimi.

"""