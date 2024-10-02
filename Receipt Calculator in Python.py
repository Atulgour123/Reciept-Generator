# Receipt Calculator in Python

class ReceiptCalculator:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity):
        self.items[name] = {"price": price, "quantity": quantity}

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["price"] * item["quantity"]
        return total

    def generate_receipt(self):
        print("Receipt:")
        for name, item in self.items.items():
            print(f"{name}: {item['quantity']} x {item['price']} = {item['price'] * item['quantity']:.2f}")
        print(f"Total: {self.calculate_total():.2f}")

def main():
    calculator = ReceiptCalculator()
    while True:
        print("1. Add item")
        print("2. Generate receipt")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            calculator.add_item(name, price, quantity)
        elif choice == "2":
            calculator.generate_receipt()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()