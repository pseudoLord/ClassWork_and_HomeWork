class Product:
    def __init__(self, name, price, availability=True, kcal=0):
        self.name = name
        self.price = price
        self.availability = availability
        self.kcal = kcal

    def __str__(self):
        return f"{self.name} - {self.price}$ ({'Available' if self.availability else 'Not available'})"

    def info(self):
        status = "Yes" if self.availability else "No"
        return f"{self.name}:\nprice - {self.price}$\nkcal - {self.kcal}\navailability - {status}"


class Cart:
    def __init__(self):
        self.items = []
        self.wallet = 20.0

    def show_products(self, products):
        print("\nProducts:")
        for product in products:
            print(product)
        print()

    def buy(self, product_name, products):
        for product in products:
            if product.name.lower() == product_name.lower():
                if product.availability:
                    self.items.append(product)
                    print(f"{product.name} added to cart.\n")
                else:
                    print(f"{product.name} currently not available.\n")
                return
        print(f"Product {product_name} Not found.\n")

    def remove_from_cart(self, product_name):
        for item in self.items:
            if item.name.lower() == product_name.lower():
                self.items.remove(item)
                print(f"{item.name} removed from cart.\n")
                return
        print(f"{product_name} not found in cart.\n")

    def info(self, product_name, products):
        for product in products:
            if product.name.lower() == product_name.lower():
                print(product.info() + "\n")
                return
        print(f"Product {product_name} not found.\n")

    def show_cart(self):
        if not self.items:
            print("Cart is empty..\n")
        else:
            print("In cart:")
            for item in self.items:
                print(f"- {item.name}")
            print()

    def total_price(self):
        return sum(item.price for item in self.items)

    def pay(self):
        total = self.total_price()
        if total == 0:
            print("Cart is empty. There is nothing to pay for.\n")
            return
        print("Payment:")
        for item in self.items:
            print(f"- {item.name}")
        print(f"Total cost: {total}$")
        answer = input("Would you like to pay? (Yes/No): ").strip().lower()
        if answer == "Yes":
            if self.wallet >= total:
                self.wallet -= total
                print(f"-{total}$, Thank you for your purchase!\n")
                self.items = []
            else:
                print("There is not enough money in the wallet.\n")
        else:
            print("Payment canceled.\n")



bread = Product("Bread", 3.4, True, 120)
cheese = Product("Chese", 2.2, False, 200)
milk = Product("Milk", 4.1, True, 55)

products = [bread, cheese, milk]
cart = Cart()

print("Welcome to the store!\n")
cart.show_products(products)

while True:
    command = input("Enter the command: ").strip().lower()

    if command == "Exit":
        print("Goodbye!")
        break
    elif command == "show products":
        cart.show_products(products)
    elif command.startswith("buy "):
        name = command.replace("buy ", "").strip()
        cart.buy(name, products)
    elif command.startswith("info "):
        name = command.replace("info ", "").strip()
        cart.info(name, products)
    elif command in ["cart", "show cart"]:
        cart.show_cart()
    elif command.startswith("delete "):
        name = command.replace("delete ", "").strip()
        cart.remove_from_cart(name)
    elif command == "pay":
        cart.pay()
    else:
        print("Unknown command. Please try again.\n")
