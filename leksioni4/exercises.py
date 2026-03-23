"""
1. Filtri i Numrave
Krijo një listë me 10 numra (manualisht).
Printo:
•	vetëm numrat çift
•	vetëm numrat më të mëdhenj se 50
"""
#inicializim i listes
"""
numrat = [20, 70, 60, 52, 48, 36, 85, 90, 100, 24]

for numri in numrat:
    if numri %2 == 0 and numri > 50:
        print(numri)
"""


"""
2. Emra Unikë

Ke këtë listë:

names = ["Ana", "Bledi", "Ana", "Sara", "Bledi"]

Detyra:

Hiq dublikatat

Printo sa emra unikë ka

Printo emrat në rend alfabetik
"""
"""
names = ["Ana", "Bledi", "Ana", "Sara", "Bledi"]

#Hiq dublikatat
names.remove("Ana")
names.remove("Bledi")

print(names)
"""

#Inicializojme listen
"""
ngjyrat = []

for ngjyra in range(1, 3):
    ngjyrat.append(input(f"Vendos ngjyren {ngjyra}: "))

print(ngjyrat)
"""

    







"""
3. Numërimi i Shkronjave
Kërko nga përdoruesi 3 emra makinash.
Printo: Numrin e karaktereve per secilen Makine

"""

makinat = ["Mercedes-benz"]


answer = "y"
while answer == "y":
    makinat.append(input("Shkruaj marken e makines: "))
    answer = input("Deshiron te shtosh nje makine tjeter? (y/n)")




for i in makinat:
    cnt = 0
    for j in i:
        if j.isalnum():
            cnt +=1

    print(f"{i} ka {cnt} gërma")




"""
4. Loja e Notave

Krijo një listë me 10 nota (0–100).

Detyra:

--> Gjej mesataren

--> Printo notën më të madhe
--> Printo notën më të vogël

--> Printo sa nxënës kalojnë (nota ≥ 50)

Mos përdor funksionet built-in si max() dhe sum().
"""


"""

5. Password Strength Checker

Kërko një password nga user.

    Kontrollo nëse:

        --> Ka të paktën 8 karaktere

        --> Ka të paktën 1 numër

        --> Ka të paktën 1 shkronjë të madhe

        -->Ka të paktën 1 simbol

    Printo:

        Weak --> Plotëson 0 - 2 kritere

        Medium  --> Plotëson 3 nga 4 kriteret

        Strong --> Plotëson të gjitha kriteret

------------------- Hint -------------------------
Metodat që mund ti përdorim:
  -- isdigit() --> True nëse karakteri është numër (0–9)
  -- isupper() --> True nëse është shkronjë e madhe
  -- isalnum() --> True nëse është shkronjë ose numër
      !!!!!!!!!--> False → nëse është diçka tjetër

password = input("Enter your password: ")

long_enough = False
has_number = False
has_upper = False
has_symbol = False
"""


"""
Ushtrimi 6: Bank Fraud Detector
Ke listën e mëposhtme të transaksioneve:
    50, 2000, 30, 5000, 70, 15000, 20 :
    Çdo numër përfaqëson një pagesë në euro.

Një transaksion konsiderohet “i dyshimtë” nëse është më i madh se 3000€.

Detyrat

    1. Gjej dhe printo të gjitha transaksionet mbi 3000€.
    2. Numëro sa transaksione të dyshimta ka.
    3. Llogarit mesataren e transaksioneve të dyshimta.
    4. Nëse ka më shumë se 2 transaksione të dyshimta → printo:
       ALERT: Suspicious activity detected


"""