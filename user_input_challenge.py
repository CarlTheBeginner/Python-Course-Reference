# 1
# rental = input("what kind of rental car you would like?: ")
# print(f"Let me see if i can find you a {rental.title()}")

# 2
# restaurant = int(input("How many people are in your group? "))
# if restaurant > 8:
#     print(f"all of you please be wait for the table!".title())
# else:
#     print("the table is ready!".title())

# 3
# num_input = int(input("Enter a number : "))
# if num_input % 2 == 0:
#     print(f"{num_input} is a multiple of 10!")
# else:
#     print(f"{num_input} is not a multiple of 10!")

# 4
# pizza = "\nEnter a toppings of pizza : "
# pizza += "\n(Enter 'quit' to end the program) "
#
# user_pizza = ""
# while user_pizza != 'quit':
#     user_pizza = input(pizza)
#     print(user_pizza)


# 5
# message = "please enter your age? : "
# active = True
# while active:
#     age = int(input(message))
#     if age <= 3:
#         print("Ticket is free!")
#         break
#     elif age <= 12:
#         print("Ticket is $10")
#         break
#     elif age > 12:
#         print("Ticket is $15")
#         break
#     else:
#         active = False

# 6
# pizza = "\nEnter a toppings of pizza : "
# pizza += "\n(Enter 'quit' to end the program) "
#
# user_pizza = ""

# while user_pizza != 'quit':
#     user_pizza = input(pizza)
#
#     if user_pizza != 'quit':
#         print(user_pizza)

# active = True
#
# while active:
#     user_pizza = input(pizza)
#     if user_pizza == 'quit':
#         active = False
#     else:
#         print(user_pizza)

# while user_pizza != 'quit':
#     user_pizza = input(pizza)
#
#     if user_pizza == 'quit':
#         break
#     else:
#         print(user_pizza)

#7
# number = 0
# while number <= 5:
#     print(number)
#     number += 1

# 8
# sandwich_orders = ['ham', 'cheese', 'pastrami', 'beef patty']
#
# finished_sandwiches = []
#
# while sandwich_orders:
#     sandwiches = sandwich_orders.pop()
#
#     print(f"I made your {sandwiches.title()}")
#
#     finished_sandwiches.append(sandwiches)
#
# print(f"sandwiches are made by following\n"
#       f" - {finished_sandwiches}")

# 9
# sandwich_orders = ['pastrami', 'ham', 'cheese', 'pastrami', 'beef patty', 'pastrami']
#
# finished_sandwiches = []
#
# while sandwich_orders:
#     sandwiches = sandwich_orders.pop()
#
#     print(f"I made your {sandwiches.title()}")
#
#     finished_sandwiches.append(sandwiches)
#
#     if 'pastrami' in finished_sandwiches:
#         finished_sandwiches.remove('pastrami')
#
# print("We have run out of pastrami!!")
# print(f"sandwiches are made by following\n"
#       f" - {finished_sandwiches}")

# 10
# dream_vacation = []
#
# poll_active = True
#
# while poll_active:
#     dream_vacay = input("If you could visit one place in the world, where would you go? : ")
#     dream_vacation.append(dream_vacay)
#
#     cont = input(f"Should you continue to answer the question? : (yes / no) ")
#     if cont == 'no':
#         poll_active = False
#
# print(f"Here are the results of the poll")
# for results in dream_vacation:
#     print(f"\t- {results}")
#


