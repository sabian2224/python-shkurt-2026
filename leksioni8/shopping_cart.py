#Online Store Shopping cart
class Product:
    
    def __init__(self, name:str, price:int, category):
        self.name = name
        self.price = price
        self.category = category.capitalize()
        self.stock = 0 #

lenovo_ideapad = Product("Lenovo Ideapad", 700, "laptop")
hp_elitebook = Product("HP Elitebook", 400, "laptop")
iPhone_17_pro_max = Product("iPhone 17 Pro Max", 1400, "smartphone")

class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = {
        }

    def add_inventory(self, product:Product, stock):
        if not product.category in self.inventory:
            self.inventory[product.category] = [product]
            product.stock = stock
        else:
            self.inventory[product.category].append(product)
            product.stock += stock
        
    def print_catalog(self):
        for category, products in self.inventory.items():
            print("-------------------------------------------------------------------")
            print(f"{category} : ")
            for product in products:
                print(f"| {product.name} ${product.price} ({product.stock})", end=" | ")
            print()
            print("-------------------------------------------------------------------")

      
            
          



pako = Store("Pako.al")
pako.add_inventory(lenovo_ideapad, 10)
pako.add_inventory(hp_elitebook, 5)
pako.add_inventory(iPhone_17_pro_max, 30)
pako.print_catalog()



class ShoppingCart:
    def __init__(self):
        self.items = {
            #product: 2
        }

    def add_to_cart(self, product:Product, qt:int=1):
        if not product in self.items:
            self.items[product] = qt
        else:
            self.items[product] += qt

    def print_cart(self):
        print("-------------------------------")
        print("Your shopping cart:")
        print("-------------------------------")
        total = 0
        for product, qt in self.items.items():
            print(f"{product.name} ${product.price} x {qt}: ${product.price * qt}")
            total += product.price * qt
        print(f"Totali = ${total}")


    def checkout(self):
        for product, qt in self.items.items():
            product.stock -= qt
        print("Checkout successful")



cart = ShoppingCart()
cart.add_to_cart(lenovo_ideapad)
cart.add_to_cart(lenovo_ideapad)
cart.add_to_cart(iPhone_17_pro_max, 3)
cart.print_cart()
cart.checkout()
pako.print_catalog()

