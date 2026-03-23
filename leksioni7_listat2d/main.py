#Leksioni 7: Nested Loops & 2D Lists

#Një nested loop është thjesht një cikël që ndodhet brenda një cikli tjetër.
#- Outer Loop
#- Inner Loop

#Shembull: Tailwind Colors: 
"""
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
for i in range(len(colors)):
    intensity = 0
    print(f"{i+1} - {colors[i]}: ", end="")
    for j in range(9):
        intensity += 100
        print(f" {intensity} ", end="")
    print()
"""



#-->Një 2D list është një listë që përmban një listë tjetër brënda saj.
"""
         +-----+-----+-----+-----+
List x = | 10  | 20  | 30  | 40  |
         +-----+-----+-----+-----+

Index      0     1      2      3
        ------------------------------

        
                Column 0   Column 1   Column 2
              +----------+----------+----------+
Row 0         |  x[0][0] |  x[0][1] |  x[0][2] |
              +----------+----------+----------+
Row 1         |  x[1][0] |  x[1][1] |  x[1][2] |
              +----------+----------+----------+
Row 2         |  x[2][0] |  x[2][1] |  x[2][2] |
              +----------+----------+----------+
"""

"""
Shembull: vendet në një kinema

A1  A2  A3  A4
B1  B2  B3  B4
C1  C2  C3  C4

"""
#1. Inicializimi i një 2D List:
"""
a = ["A1", "A2", "A3", "A4"]
b = ["B1", "B2", "B3", "B4"]
c = ["C1", "C2", "C3", "C4"]

cinema = [a, b, c]

#2. Printimi i një 2D List:
#2.1: Duke perdorur metoden print():
print(cinema)
"""
#2.2: Duke iteruar me for loop:
#Duke printuar me nje loop te vetem:
#print(cinema[2][2])

#Duke printuar me 2 loops:
"""
for i in range(len(cinema)):
    print(f"Row: {i+1}")
    for j in range(len(cinema[i])):
        print(f"{cinema[i][j]}", end=" ")
    print()
"""
#3. Aksesimi i elementeve
#cinema[1][1] = "Reserved"

#4. Ndryshimi i nje elementi:

#5.Marrja e input-it nga përdoruesi
"""
row = int(input("Enter row: "))
column = int(input("Enter seat: "))

cinema[row][column] = "X"
"""
#6.Iterimi në një 2D list

#7. Krijimi i listes me user input
"""
rows_length = int(input("Vendos numrin e rreshtave: "))
cols_length = int(input("Vendos numrin e kolonave: "))
numrat = []

for i in range(rows_length):
    temp_list = []
    print(f"Rreshti {i+1}:")
    for j in range(cols_length):
        temp_list.append(int(input(".._"))) 
    numrat.append(temp_list)

print(numrat)"""

"""
Ushtrimi1:
Krijo një 2D list 3x3 me numra dhe printoje në formë tabele.

Output shembull:
1 2 3
4 5 6
7 8 9

"""


"""
Ushtrimi2:
Krijo një 2D list dhe gjej numrin më të madh në matrix.
Output:
Max = 98
"""
#1. Lista meret si input nga useri
"""
rows_length = int(input("Vendos numrin e rreshtave:"))
cols_length = int(input("Vendos numrin e kolona:"))
matrix = []
for i in range(rows_length):
    print(f"Rreshti {i}:")
    temp_list = []
    for j in range(cols_length):
        temp_list.append(int(input(".._")))
    matrix.append(temp_list)
"""


#2.Gjejme vleren max
"""
max_ = matrix[0][0]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if max_ < matrix[i][j]:
            max_ = matrix[i][j]
print(f"Max Value = {max_}")"""


#3.Gjejme shumen per secilin rresht
"""
for i in range(len(matrix)):
    shuma = 0
    for j in range(len(matrix[i])):
        shuma += matrix[i][j]
    print(f"Rreshti {i}, Shuma = {shuma}")
  """



"""
Ushtrimi 3:
Krijo një program në python që merr si input nga useri 
një listë 2d dhe printon shumën e çdo rreshti.

Shembull:

1 2 3
4 5 6
7 8 9

Output:

Row 1 sum = 6
Row 2 sum = 15
Row 3 sum = 24
"""

"""
Ushtrimi 4:  Shuma e çdo kolone
Krijo një program në python që merr si input nga useri 
një listë 2d dhe printon shumën e çdo kolone.

Output:

Column 1 sum = 12
Column 2 sum = 15
Column 3 sum = 18

"""

"""
Ushtrimi 5:

Krijo një matrix NxN dhe printo diagonalën kryesore.

Shembull:

1 2 3
4 5 6
7 8 9

Output:

1 5 9

"""

"""
Ushtrimi 6: Numrat çift

Krijo një 2D list dhe numëro sa numra çift (even numbers) ka në matrix.

Output:

Even numbers = 7

"""


"""
Ushtrimi 7

Useri jep madhësinë n.

Output:

*
* * 
* * *
* * * *

"""

"""
Ushtrimi 8: 
Useri jep madhësinë n.

Output:

* 
* * 
* * * 
* * * *
"""



"""
Ushtrim: Sistemi i Kinemasë

Detyra: Krijo një program që menaxhon një sallë kinemaje me 25 vende.
 Për këtë, përdor një 2D List (matricë 5x5). Fillimisht,
    të gjitha vendet janë shënuar me shkronjën **"L"** (Lirë).
Kur rezervohen, bëhen **"Z"** (Zënë).

Programi duhet të shfaqë një meny me 4 opsione që përsëritet vazhdimisht:

1. Shfaq sallën: Printo matricën në formë rrjete (grid).
2. Rezervo: Kërko rreshtin (0-4) dhe kolonën (0-4). Nëse vendi është "L", ktheje në "Z". Nëse është "Z", afisho një mesazh që vendi është i zënë.
3. Statistika: Numëro sa "L" dhe sa "Z" ka në total.
4. Dil: Mbyll programin.

---

Shembull i Output-it

--- MENYJA E KINEMASË ---
1. Shfaq sallën
2. Rezervo
3. Statistika
4. Dil
Zgjidh një opsion: 1

L L L L L 
L L L L L 
L L L L L 
L L L L L 
L L L L L 

--- MENYJA E KINEMASË ---
Zgjidh një opsion: 2
Fut rreshtin (0-4): 2
Fut kolonën (0-4): 3
Rezervimi u krye me sukses!

--- MENYJA E KINEMASË ---
Zgjidh një opsion: 1

L L L L L 
L L L L L 
L L L Z L 
L L L L L 
L L L L L 
--- MENYJA E KINEMASË ---
Zgjidh një opsion: 3
Vende të lira: 24
Vende të zëna: 1
"""

#Hapi1: Ndertimi i matrices
cinema = [
    ["A1", "A2", "A3", "A4", "A5"],
    ["B1", "B2", "B3", "B4", "B5"],
    ["C1", "C2", "C3", "C4", "C5"],
    ["D1", "D2", "D3", "D4", "D5"],
    ["E1", "E2", "E3", "E4", "E5"]
]

#Hapi 2: Krijimi i funksioneve te programit
def print_cinema(cinema):
     for i in range(len(cinema)):
        for j in range(len(cinema[i])):
            print(f"{cinema[i][j]}  ", end="")
        print()

def print_stats(cinema):
     reserved_seats = 0
     free_seats = 0
     for i in range(len(cinema)):
        for j in range(len(cinema[i])):
            if cinema[i][j] != "XX":
                free_seats += 1 
            else:
                reserved_seats += 1
     print(f"Poltrona te lire: {free_seats}")
     print(f"Poltrona te rezervuar: {reserved_seats}")

def choose_seat(cinema):
    choose_method = input("Zgjidh ulesen rastesore(r) / specifikoje (s):")
    if choose_method ==  "r":
        for i in range(len(cinema)):
            for j in range(len(cinema[i])):
                if cinema[i][j] != "XX":
                    print(f"Poltroni juaj u rezervua: {cinema[i][j]}")
                    cinema[i][j] = "XX"
                break
            break
    elif choose_method == "s":
        print_cinema(cinema)
        choose_seat = input("Zgjidh poltronin: ")
        for i in range(len(cinema)):
            for j in range(len(cinema[i])):
                if cinema[i][j] == choose_seat and choose_seat != "XX":
                    reserved_seat = cinema[i][j]
                    print(f"Poltroni juaj u rezervua: {reserved_seat}")
                    cinema[i][j] = "XX"


while True:

    print("--- MENUJA E KINEMASË ---")
    print("1. Shfaq sallën")
    print("2. Rezervo")
    print("3. Statistika")
    print("4. Dil")
    op = int(input("Zgjidh një opsion: "))

    if op == 1:
        print_cinema(cinema)
    elif op == 2:
      choose_seat(cinema)

    elif op == 3:
       print_stats(cinema)
    elif op == 4: 
        break
    else:
        print("Komanda nuk ekziston.")


