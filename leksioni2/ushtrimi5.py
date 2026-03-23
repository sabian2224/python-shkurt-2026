car_type = "diesel"
emission_level = 30
day = "weekday"

if car_type == "electric":
    print("Entry Allowed")

elif car_type == "electric" and emission_level < 30:
    print("Entry Allowed")

elif car_type == "diesel" or car_type == "petrol":
    if day == "weekend":
        print("Entry Allowed")
    else:
        print("Entry Denied")

else: 
    print("Entry Denied")

     