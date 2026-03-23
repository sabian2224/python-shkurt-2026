"""
Ushtrimi 1: Numërim Bazë

--> Printo numrat nga 1 deri në 20 në një rresht të vetëm.

"""

"""
Ushtrimi 2: Numërim Mbrapsht

--> Printo numrat nga 20 deri në 1.
"""

"""
Ushtrimi 3: Shuma e Numrave

Kërko nga përdoruesi një numër n.
Printo shumën e numrave nga 1 deri në n.

Shembull:

Input: 5
Output: 15


"""

"""
Ushtrimi 4: Vetëm Shuma e Numrave Çift

Kërko nga përdoruesi një numër n.
Printo shumën vetëm të numrave çift nga 1 deri në n.

"""


"""
Ushtrimi 5: Hyrje me PIN (3 Përpjekje)

Problemi: Krijo një program që i kërkon përdoruesit të vendosë një PIN.

* PIN-i i saktë = 4321
* Përdoruesi ka 3 perpjekje

Pas çdo përpjekjeje të gabuar shfaq:
--> "PIN i gabuar. Përpjekje të mbetura: X"

Nëse PIN-i është i saktë:
--> "Ju u loguat me sukses." dhe programi ndalon.

Nëse të gjitha përpjekjet dështojnë:
--> "Karta u bllokua"

"""


""" 
Ushtrimi6: Tërheqje nga ATM (Cikël me Validim)

Problemi: Ndërto një program për tërheqje nga ATM.

--> Gjendja fillestare = 500

--> Kërko shumën që do tërhiqet

Rregullat:

--> Shuma duhet të jetë pozitive

--> Duhet të jetë shumëfish i 10

Nuk duhet të kalojë gjendjen

Nëse është e pavlefshme, printo arsyen dhe kërko sërish.
Kur është e vlefshme, zbrit shumën dhe printo gjendjen e re, pastaj ndalo.

Gabime tipike për testim: -20, 0, 37, 600.
"""



"""
Ushtrimi7: Fatura e Energjisë Elektrike

Shkruaj një program që:

1) Kërkon nga përdoruesi:
    --> Emrin e klientit
    --> Njësitë e konsumuara (kWh)

    Nëse kWh është negativ, shfaq gabim dhe kërko sërish derisa të jetë ≥ 0


2) Llogarit faturën me tarifim progresiv (me nivele)

Tarifat sipas intervaleve:

    --> 0 – 200 kWh → 0.10 $ / kWh
    --> 201 – 500 kWh → 0.12 $ / kWh
    --> Mbi 500 kWh → 0.15 $ / kWh

3) Taksa

Vendos një limit pa taksë:

--> Nëse totali ≤ 100$ → taksa = 0
--> Nëse totali > 100$ → taksa aplikohet vetëm mbi pjesën që kalon 100$

Norma e taksës: 8%

4) Printo në fund:

* Emri i klientit
* kWh të konsumuara
* Totali para taksës
* Pjesa e tatueshme (nëse ka)
* Shuma e taksës
* Fatura finale (totali + taksa)
"""
