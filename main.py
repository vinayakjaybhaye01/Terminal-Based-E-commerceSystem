import json
import os
from utils.helper import encrypt_password, decrypt_password, generate_key


# generate_key()

class Product:
    def __init__(self, product_id, name, price, stock=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        # if stock is available 
        if self.stock is not None:
            return f"{self.product_id}: {self.name} - ${self.price:.2f} (Stock: {self.stock})"
        else:
            return f"{self.product_id}: {self.name} - ${self.price:.2f}"



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []
        self.order_history = []

    def add_to_cart(self, product):
        if product.stock > 0:
            self.cart.append(product)
            product.stock -= 1
            print(f"{product.name} added to cart.")
        else:
            print("Sorry, this product is out of stock!")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for index, product in enumerate(self.cart, start=1):
              if product.stock is not None:  # Check if stock is not None
                 print(f"{index}. {product.name} - ${product.price} (Stock left: {product.stock})")
              else:
                 print(f"{index}. {product.name} - ${product.price}") 


    def place_order(self):
        if len(self.cart) == 0:
            print("Your cart is empty!")
            return
        self.order_history.append(self.cart[:])
        self.cart.clear()
        print("Order placed successfully!")

    def view_order_history(self):
        if not self.order_history:
            print("No orders placed yet.")
            return
        print("Order History:")
        for index, order in enumerate(self.order_history, start=1):
            print(f"Order {index}:")
            for product in order:
                print(f"  - {product}")

    def to_dict(self):
        #convert user object to dict to save
        return {
            'username': self.username,
            'password': encrypt_password(self.password).decode(),
            'cart': [{'product_id': product.product_id, 'name': product.name, 'price': product.price} for product in self.cart],
            'order_history': [
                [{'product_id': product.product_id, 'name': product.name, 'price': product.price} for product in order]
                for order in self.order_history
            ]
        }

    @staticmethod
    def from_dict(user_data):
        #create user object from dict saved in file
        user = User(user_data['username'], decrypt_password(user_data['password'].encode()))
        user.cart = [Product(**item) for item in user_data['cart']]
        user.order_history = [[Product(**item) for item in order] for order in user_data['order_history']]
        return user


class ECommerceSystem:
    def __init__(self):
        self.products = []
        self.users = {}
        self.load_products()
        self.load_users()

    def load_products(self):
        if os.path.exists('utils/products.json'):
            with open('utils/products.json', 'r') as f:
                products_data = json.load(f)
                for product_info in products_data:
                    product = Product(
                        product_info['product_id'],
                        product_info['name'],
                        product_info['price'],
                        product_info['stock']
                    )
                    self.products.append(product)

    def save_products(self):
        products_data = [
            {
                'product_id': product.product_id,
                'name': product.name,
                'price': product.price,
                'stock': product.stock
            }
            for product in self.products
        ]
        with open('utils/products.json', 'w') as f:
            json.dump(products_data, f, indent=4)

    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as f:
                users_data = json.load(f)
                for username, user_info in users_data.items():
                    self.users[username] = User.from_dict(user_info)

    def save_users(self):
        users_data = {username: user.to_dict() for username, user in self.users.items()}
        with open('users.json', 'w') as f:
            json.dump(users_data, f, indent=4)

    def add_product(self, product):
        self.products.append(product)
        self.save_products()


    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists!")
            return
        self.users[username] = User(username, password)
        self.save_users()
        print("User registered successfully!")

    def login_user(self, username, password):
        if username not in self.users:
            print("User not found!")
            return None
        user = self.users[username]
        if user.password != password:
            print("Incorrect password!")
            return None
        print(f"Welcome, {username}!")
        return user


def main():
    system = ECommerceSystem()
    
    while True:
        print("\n--- E-Commerce System ---")
        print("1. Register")
        print("2. Login")
        print("3. View Products")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("Type 'cancel' to cancel registeration")
            username = input("Enter username: ")
            
            if(username.lower() != 'cancel'):
               password = input("Enter password: ")
               if(password.lower() != 'cancel'): 
                 system.register_user(username, password)
               else:
                 print("Registration cancelled")
            else:
                print('registeration cancelled')


        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = system.login_user(username, password)
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Add Product to Cart")
                    print("2. View Cart")
                    print("3. Place Order")
                    print("4. View Order History")
                    print("5. Logout")
                    sub_choice = input("Choose an option: ")

                    if sub_choice == '1':
                        print("\nAvailable Products:")
                        for index, product in enumerate(system.products, start=1):
                            print(f"{index}. {product.name} - ${product.price} (Stock: {product.stock})")

                        product_index = input("Select product by number: ")
                        if product_index.isdigit():
                            product_index = int(product_index) - 1
                            if 0 <= product_index < len(system.products):
                                product = system.products[product_index]
                                user.add_to_cart(product)
                                system.save_users()
                                
                            else:
                                print("Invalid product selection!")
                        else:
                            print("Please enter a valid number.")
                    
                    elif sub_choice == '2':
                        user.view_cart()
                    elif sub_choice == '3':
                        user.place_order()
                        system.save_users()
                        system.save_products()
                        
                    elif sub_choice == '4':
                        user.view_order_history()
                    elif sub_choice == '5':
                        print("Logging out...")
                        system.save_users()
                        system.save_products()
                        break
                    else:
                        print("Invalid choice!")
        elif choice == '3':
            print("\nAvailable Products:")
            for product in system.products:
                print(product)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
