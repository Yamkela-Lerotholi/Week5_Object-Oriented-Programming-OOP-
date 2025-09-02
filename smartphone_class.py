class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        print(f"Making a call to {number}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

# Inheritance
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, price, camera_quality, battery_life):
        super().__init__(brand, model, price)  # Call the constructor of the parent class
        self.camera_quality = camera_quality
        self.battery_life = battery_life

    # Overriding the display_info method to include new attributes
    def display_info(self):
        super().display_info()  # Call the parent method
        print(f"Camera Quality: {self.camera_quality} MP, Battery Life: {self.battery_life} hours")

# Create instances
phone1 = Smartphone("Apple", "iPhone 13", 799)
phone2 = AdvancedSmartphone("Samsung", "Galaxy S21", 999, 108, 24)

phone1.display_info()
phone2.display_info()
