#Hapi1: Inicializimi i variablave
#"electric", "hybrid", "diesel", "petrol"
car_type = "electric"
emission_level = 30 #1 - 100
day = "Weekday" #Weekday / Weekend


#Hapi 2: Krijojme logjiken e programit
"""
1.Nëse makina është "electric" → lejohet gjithmonë
2.Nëse është "hybrid" → lejohet vetëm nëse emission_level < 50
3.Nëse është "diesel" ose "petrol":
  Lejohet vetëm nëse është weekend DHE emission_level < 30
  Përndryshe → hyrja ndalohet
"""
if car_type == "electric":
    print("Entry Allowed")
elif car_type == "hybrid" and emission_level < 50:
    print("Entry Allowed")

elif car_type == "diesel" or car_type == "petrol":
    if day == "Weekend" and emission_level < 30:
        print("Entry Allowed")
    else:
        print("Entry Denied")
else:
    print("Entry Denied")

