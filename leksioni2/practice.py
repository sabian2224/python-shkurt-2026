play_again = "n"

name = input("Customer Name:")#name
kwh = int(input("Units Consumed:"))#Units KWH
#this input() functions always returns a string
#Because input() reads text from the terminal.
#The terminal doesn’t know math., It only knows characters.
calculated_price = 0
total_price = 0
tax = 0


#testing phase
"""""
print(f"Name: {name}")
print(f"Units consumed: {kwh} kWh")
"""""

#logic
"""""
0 - 200 --> $0.10 per kWh
201 - 500 --> $0.12 per kWh
Above 500 --> $0.15 per kWh
"""""

#if total bill > $100 -> add 8% tax

if (kwh >= 0 and kwh < 201):
    calculated_price = kwh * 0.10
    total_price = calculated_price

elif kwh > 200 and kwh <= 500:
    calculated_price = kwh * 0.12
    total_price = calculated_price

elif kwh > 500:
    calculated_price = kwh * 0.15
    if calculated_price > 100:
        tax = calculated_price * 0.08
        total_price = calculated_price + tax





print(f"Customer name: {name} \nTotal Price: ${total_price}  \nTAX: ${tax}")


while play_again == "y": 
    name = input("Customer Name:")#name
    kwh = int(input("Units Consumed:"))#Units KWH
    #this input() functions always returns a string
    #Because input() reads text from the terminal.
    #The terminal doesn’t know math., It only knows characters.
    calculated_price = 0
    total_price = 0
    tax = 0


    #testing phase
    """""
    print(f"Name: {name}")
    print(f"Units consumed: {kwh} kWh")
    """""

    #logic
    """""
    0 - 200 --> $0.10 per kWh
    201 - 500 --> $0.12 per kWh
    Above 500 --> $0.15 per kWh
    """""

    #if total bill > $100 -> add 8% tax

    if (kwh >= 0 and kwh < 201):
        calculated_price = kwh * 0.10
        total_price = calculated_price

    elif kwh > 200 and kwh <= 500:
        calculated_price = kwh * 0.12
        total_price = calculated_price

    elif kwh > 500:
        calculated_price = kwh * 0.15
        if calculated_price > 100:
            tax = calculated_price * 0.08
            total_price = calculated_price + tax





    print(f"Customer name: {name} \nTotal Price: ${total_price}  \nTAX: ${tax}")
    play_again = input("Do you want to play again? (y/n)")
