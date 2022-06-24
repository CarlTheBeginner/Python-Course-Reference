# 1.
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("Is car == 'audi'? I predict False.")
# print(car == 'audi')
# print("Is car != 'audi' I Predict True")
# print(car != 'audi')
# car = 'audi'
# print("Is car == 'audi' I Predict True")
# print(car == 'audi')
# print("Is car.title() == 'audi' I Predict True")
# print(car.title() == 'audi')
#
# car = 'Range Rover'
# print("Is car != 'audi' I Predict True")
# print(car != 'audi')
# print("Is car.lower() 'audi' I Predict True")
# print(car.lower() == 'audi')
# print("Is car != 'audi' I Predict True")
# print(car != 'audi')
# print("Is car != 'audi' I Predict True")
# print(car == 'audi')
# print("Is car != 'audi' I Predict True")
# print(car == 'RANGE ROVER')

# TODO : Check conditional test cases
# 2.
# car = 'Range Rover'
# print(car == 'range rover')
# print(car.lower() == 'range rover')
#
# num = 20
# print(num < 25)
# print(num > 25)
# print(num >= 25)
# print(num <= 25)
# print(num <= 25 or num >= 25)
# print(num <= 25 and num >= 25)
#
# names = ['shane', 'anthony', 'james', 'calderon']
# print('shane' in names)
# print('shane' not in names)

# 3.
# alien_color = ['green', 'yellow', 'red']
# points = 0
# if 'green' in alien_color:
#     points = 5
#
# print(f"you just earned {points} point/s.")

# alien_color = ['green', 'yellow', 'red']
# points = 0
# if 'black' in alien_color:
#     points = 5
# else:
#     print("No Output")
#
# print(f"you just earned {points} point/s.")


# 4.
# alien_color = ['green', 'yellow', 'red']
# points = 0
# if 'black' in alien_color:
#     points = 5
# else:
#     points = 10
#
# print(f"You just earned {points} point/s")

# 5.
# alien_color = ['green', 'yellow', 'red']
#
# points = 0
# if 'green' in alien_color:
#     points = 5
# elif 'yellow' in alien_color:
#     points = 10
# elif 'red' in alien_color:
#     points = 15
# else:
#     print("none")
#
#
# print(f"You have {points} point/s")

# 6.
# age = 71
#
# if age < 2:
#     print("BABY")
# elif age <= 4:
#     print("TODDLER")
# elif age <= 13:
#     print("KID")
# elif age <= 20:
#     print("TEENAGER")
# elif age <= 65:
#     print("ADULT")
# else:
#     print("ELDER")

# 7.
# fruits = ['kiwi', 'strawberry', 'orange']
#
# if 'kiwi' in fruits:
#     print("You really like kiwi".upper())
# if 'strawberry' in fruits:
#     print("You really like strawberry".upper())
# if 'orange' in fruits:
#     print("You really like orange".upper())
# if 'mango' in fruits:
#     print("You really like mango".upper())
# if 'banana' in fruits:
#     print("You really like banana".upper())

# 8-9
# usernames = ['james123', 'carlcool23', 'mikeymike10', 'edwinthegreat12', 'masterfeat', 'admin']
#
# # this will check if the user list is empty
# if usernames:
#     for username in usernames:
#         # this whill check if the admin is in the list
#         if username == 'admin':
#             print(f"Hello Admin would you like to see a status report")
#         else:
#             print(f"Hello {username.title()}, thank you for logging again....")
# else:
#     print("We need to find some users!!!!")

# 10
# current_users = ['mike', 'james', 'carl', 'edward', 'jonas']
# new_users = ['jay', 'mark', 'jonas', 'carl', 'edward']
#
# current_low = [n.lower() for n in current_users] # mutates the value from list to uppercase
# new_low = [nl.lower() for nl in new_users] # these too.
#
# for new_user in new_low:
#     if new_user in current_low:
#         print(f"{new_user.title()} is used and not available!")
#     else:
#         print(f"{new_user.title()} username is available")


# 11.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for num in nums:
#     if num == 1:
#         print(f"{num}st")
#     elif num == 2:
#         print(f"{num}nd")
#     elif num == 3:
#         print(f"{num}rd")
#     else:
#         print(f"{num}th")

