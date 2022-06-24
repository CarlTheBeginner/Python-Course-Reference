import random

#
# class Die:
#     def __init__(self):
#         self.sides = 6
#
#     def roll_die(self):
#         i = 0
#         while i <= 10:
#             print(randint(1, self.sides))
#             i += 1
#
# roll_dice = Die()
# roll_dice.roll_die()

# TODO 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
#     the kind of lottery you just modeled. Make a list or tuple called my_ticket.
#     Write a loop that keeps pulling numbers until your ticket wins. Print a message
#     reporting how many times the loop had to run to give you a winning ticket.

# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# letters = ['a', 'b', 'c', 'd', 'e']
#
# my_ticket = 'c5'
#
# counter = 0
#
# win_ticket = ''
#
# def generate_ticket():
#     random_number = numbers[random.randint(0, len(numbers) - 1)]
#     random_letter = letters[random.randint(0, len(letters) - 1)]
#     return random_letter + random_number
#
#
# while True:
#     win_ticket = generate_ticket()
#     print(f"Current ticket : {win_ticket}")
#
#     counter += 1
#     if win_ticket == my_ticket:
#         print(f"It took {counter} attempts")
#         break


# TODO Random Password Generator
# four_letters = ['abcdYtU', 'aCvD', 'ZyTr', 'pOgg', 'KiLq',
#                 'ZxiOPlNs', 'YrQQ', 'PLacE', 'aWrt', 'RtYu',
#                 'IoPt']
# four_numbers = ['3215', '9888', '1029', '3309', '7645',
#                 '3292', '1234', '2456', '2311', '6843',
#                 '2455']
# special_chars = ['!', '@', '#', '$', '%',
#                  '^', '&', '*', '(', '_',
#                  '~~~', '[]']
#
# class Password:
#     def __init__(self, letters, numbers, chars):
#         self.letters = letters
#         self.numbers = numbers
#         self.chars = chars
#
#     def generate_password(self):
#         random_letters = self.letters[random.randint(0, len(self.letters) - 1)]
#         random_numbers = self.numbers[random.randint(0, len(self.numbers) - 1)]
#         random_chars = self.chars[random.randint(0, len(self.chars) - 1)]
#
#         new_password = random_chars + random_letters + random_numbers
#         print(new_password)
#
#
# new_user = Password(four_letters, four_numbers, special_chars)
# new_user.generate_password()
#

