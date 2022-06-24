class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}, a {self.cuisine_type}-style restaurant")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open for customers!!")

    def read_number_served(self):
        print(f"We have served {self.number_served} customers this day")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, customers):
        self.number_served += customers


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['cheese', 'chocolate', 'mocha', 'vanilla']

    def display_flavors(self):
        print(f"These is the list of flavors in the {self.restaurant_name}")
        for flavors in self.flavors:
            print(f"- {flavors}")


