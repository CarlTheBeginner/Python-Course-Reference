# 1 - 2
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"Welcome to {self.restaurant_name}, a {self.cuisine_type}-style restaurant")
#
#     def open_restaurant(self):
#         print(f"The {self.restaurant_name} is open for customers!!")

# restaurant1 = Restaurant('Pizza by alfredo', 'italian')
# print(f"This is {restaurant1.restaurant_name}")
# print(f"We do {restaurant1.cuisine_type} style of cuisine")
# restaurant1.describe_restaurant()
# restaurant1.open_restaurant()

# restaurant1 = Restaurant('Pizza by alfredo', 'italian')
# restaurant1.describe_restaurant()
#
# restaurant2 = Restaurant('Captains Daughter', 'Pub and steakhouse')
# restaurant2.describe_restaurant()
#
# restaurant3 = Restaurant('heart attack grill', 'burger')
# restaurant3.describe_restaurant()

# 3
# class User:
#     def __init__(self, first_name, last_name, age, birthday):
#         self.first = first_name
#         self.last = last_name
#         self.age = age
#         self.birthday = birthday
#
#     def describe_user(self):
#         print(f"User information: \n"
#               f"FULL NAME : {self.first} {self.last}\n"
#               f"AGE       : {self.age}\n"
#               f"BIRTHDAY  : {self.birthday}")
#
#     def greet_user(self):
#         print(f"Hello and Welcome, User : {self.first}")

# user1 = User('carl', 'ballenas', 21, 'October 25 2000')
# user1.describe_user()
# user1.greet_user()


# 4
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"Welcome to {self.restaurant_name}, a {self.cuisine_type}-style restaurant")
#
#     def open_restaurant(self):
#         print(f"The {self.restaurant_name} is open for customers!!")
#
#     def read_number_served(self):
#         print(f"We have served {self.number_served} customers this day")
#
#     def set_number_served(self, served):
#         self.number_served = served
#
#     def increment_number_served(self, customers):
#         self.number_served += customers
#
#
# restaurant = Restaurant('Pizza by alfredo', 'italian')
# restaurant.describe_restaurant()
#
# restaurant.set_number_served(10)
# restaurant.read_number_served()
#
# restaurant.increment_number_served(10)
# restaurant.read_number_served()


# 5
# class User:
#     def __init__(self, first_name, last_name, age, birthday):
#         self.first = first_name
#         self.last = last_name
#         self.age = age
#         self.birthday = birthday
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f"User information: \n"
#               f"FULL NAME : {self.first} {self.last}\n"
#               f"AGE       : {self.age}\n"
#               f"BIRTHDAY  : {self.birthday}")
#
#     def greet_user(self):
#         print(f"Hello and Welcome, User : {self.first}")
#
#     def display_login_attempts(self):
#         """A method to display the value of login_attempts (incremented / reset) value"""
#         print(f"You attempted to login {self.login_attempts} times!")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         print("ATTEMPTS ARE RESET")
#
#
#
# user1 = User('carl', 'ballenas', 21, 'October 25 2000')
# user1.describe_user()
# user1.greet_user()
#
# # Incrementing the login attempts 3 times
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# ################################
#
# user1.display_login_attempts()
# user1.reset_login_attempts()
# user1.display_login_attempts()

# 6
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"Welcome to {self.restaurant_name}, a {self.cuisine_type}-style restaurant")
#
#     def open_restaurant(self):
#         print(f"The {self.restaurant_name} is open for customers!!")
#
#     def read_number_served(self):
#         print(f"We have served {self.number_served} customers this day")
#
#     def set_number_served(self, served):
#         self.number_served = served
#
#     def increment_number_served(self, customers):
#         self.number_served += customers
#
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['cheese', 'chocolate', 'mocha', 'vanilla']
#
#     def display_flavors(self):
#         print(f"These is the list of flavors in the {self.restaurant_name}")
#         for flavors in self.flavors:
#             print(f"- {flavors}")
#
#
# ice_cream = IceCreamStand('Uncle Derrys', 'Ice cream parlor')
# ice_cream.describe_restaurant()
# ice_cream.display_flavors()

# 7 - 8
# class User:
#     def __init__(self, first_name, last_name, age, birthday):
#         self.first = first_name
#         self.last = last_name
#         self.age = age
#         self.birthday = birthday
#
#     def describe_user(self):
#         print(f"User information: \n"
#               f"FULL NAME : {self.first} {self.last}\n"
#               f"AGE       : {self.age}\n"
#               f"BIRTHDAY  : {self.birthday}")
#
#     def greet_user(self):
#         print(f"Hello and Welcome, User : {self.first}")
#
# class Privileges:
#     """Storing the list of privileges to the attribute..."""
#     def __init__(self, privileges=("Can add post", "Can delete post", "Can ban user")):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         """show all the privileges by using forloop"""
#         print("The user can do the following: ")
#         for privs in self.privileges:
#             print(privs)
#
# class Admin(User):
#     def __init__(self, first_name, last_name, age, birthday):
#         super().__init__(first_name, last_name, age, birthday)
#         self.privilege = Privileges()
#
# new_user = Admin('carl', 'ballenas', 21, 'oct 25')
# new_user.describe_user()
# new_user.privilege.show_privileges()


# 9
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
#     def __init__(self, battery_size=60):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kWh battery")
#
#
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         # TODO Solution to challenge 9-9
#         if self.battery_size == 60:
#             range = 140
#         elif self.battery_size == 85:
#             range = 185
#
#         print(f"This car can go about {range} miles on a full charge")
#
#     def upgrade_battery(self):
#         # TODO Solution to challenge 9-9
#         if self.battery_size == 60:
#             self.battery_size = 85
#             print("Battery Upgraded")
#         else:
#             print("The battery is already upgraded")
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
#
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
#
# my_tesla.battery.get_range()
