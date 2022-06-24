# class Dog:
#     """A simple attempt to model a Dog"""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting")
#
#     def roll_over(self):
#         """Simulate rolling over in response in command"""
#         print(f"{self.name} rolled over")
#
# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)
#
# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
#
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()
#


# class Car:
#     """A simple attempt to represent a car"""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_rating = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing in the car's mileage"""
#         print(f"This car has a {self.odometer_rating} miles in it")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer rating to the given value
#         Reject the change if it attempts to roll the odometer back
#         """
#         if mileage >= self.odometer_rating:
#             self.odometer_rating = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer rating"""
#         self.odometer_rating += miles
#
#
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


# TODO Inheritance
# class Car:
#     """A simple attempt to represent a car"""
#
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_rating = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing in the car's mileage"""
#         print(f"This car has a {self.odometer_rating} miles in it")
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer rating to the given value
#         Reject the change if it attempts to roll the odometer back
#         """
#         if mileage >= self.odometer_rating:
#             self.odometer_rating = mileage
#         else:
#             print("You can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer rating"""
#         self.odometer_rating += miles
#
# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#     def __init__(self, battery_size=75):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery")
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#
#         print(f"This car can go about {range} miles on a full charge")
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electrical vehicles."""
#
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#     def fill_gas_tank(self):
#         """Electric car don't have gas tanks."""
#         print("This car doesn't need a gas tank")
#
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

def addition(num):
    try:
        if num == '-':
            num -= 1
        else:
            num += 1
    except ValueError:
        return False
    print(num)

addition(0)
addition(9)
addition(-3)

