
# 1.
# person = {
#     'first_name': 'Carl',
#     'last_name': 'Ballenas',
#     'age': 21,
#     'city': 'Binangonan'
# }
#
# print(person)

# 2.
# fav_nums = {
#     'carl': 25,
#     'james': 7,
#     'edwin': 2,
#     'kyle': 10,
#     'mark': 20
# }
# for name, numbers in fav_nums.items():
#     print(name, numbers)

# 3.
# glossary = {
#     'if-else': 'checks if the condition is met',
#     'lists': 'used to store multiple elements(string, numbers)',
#     'tuples': 'same as lists but cannot be changed / immutable',
#     '!= operator': 'checks if the value is not equal to another value',
#     'or operator': 'checks if either one of them are true or false'
# }
#
# for word, meaning in glossary.items():
#     print(f"{word}\n"
#           f"- {meaning}\n")

# 4.
# glossary = {
#     'if-else': 'checks if the condition is met',
#     'lists': 'used to store multiple elements(string, numbers)',
#     'tuples': 'same as lists but cannot be changed / immutable',
#     '!= operator': 'checks if the value is not equal to another value',
#     'or operator': 'checks if either one of them are true or false',
#     'keys()': 'access the keys inside the dictionary',
#     'items()': 'access the keys and values in the dictionary',
#     'values()': 'access the value in the dictionary',
#     'pop()': 'remove the last element on the list',
#     'insert()': 'inserts a value and specific position in the list',
#
# }
#
# for word, meaning in glossary.items():
#     print(f"{word}\n"
#           f"- {meaning}\n")

# 5
# rivers = {
#     'nile': 'egypt',
#     'yangtze': 'china',
#     'amazon': 'brazil'
# }
#
# for river, country in rivers.items():
#     print(f"The {river.title()} runs through {country.title()}")
#
# for river in rivers.keys():
#     print(river)
#
# for country in rivers.values():
#     print(country)

# 6
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
#
# take_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'james': 'cpp',
#     'mike': 'cs'
# }
#
# for name in favorite_languages.keys():
#     if name in take_languages.keys():
#         print(f"{name} thanks for responding")
#     else:
#         print(f"{name} i invite you to take to the polls!")

# 7
# person_1 = {
#     'first_name': 'carl',
#     'last_name': 'ballenas',
#     'age': 21,
#     'city': 'binangonan'
# }
#
# person_2 = {
#     'first_name': 'mike',
#     'last_name': 'jones',
#     'age': 18,
#     'city': 'cavite'
# }
#
# person_3 = {
#     'first_name': 'jim',
#     'last_name': 'halpert',
#     'age': 30,
#     'city': 'scranton'
# }
#
# people = [person_1, person_2, person_3]
#
#
# for p in people:
#     print(p)


# 8
# pets = {
#     'carl': ['dog', 'cat']
# }
#
# for name, pet in pets.items():
#     print(f"his name is {name}")
#     print("and his pets are:")
#     for p in pet:
#         print(f"\t {p}")

# 9
# favorite_places = {
#     'james': ['enchanted kingdom', 'star city', 'boracay'],
#     'mike': ['subic', 'baguio'],
#     'kyle': ['laiya', 'paris']
# }
#
# for name, places in favorite_places.items():
#     print(f"{name.title()} places are:")
#     for place in places:
#         print(f"\t{place.title()}")


# 9.
# fav_nums = {
#     'carl': [25, 12, 3, 12, 13],
#     'james': [7, 11, 4, 11, 14],
#     'edwin': [2, 9, 5, 10, 15],
#     'kyle': [10, 14, 6, 9, 16],
#     'mark': [20, 8, 7, 8, 17]
# }
# for name, numbers in fav_nums.items():
#     print(f"{name.title()} numbers are : ")
#     for number in numbers:
#         print(F"\t {number}")


# 10
# cities = {
#     'beijing': {
#         'country': 'china',
#         'population': 1_441_500_000,
#         'fact': 'china has invented coronavirus'
#     },
#     'manila': {
#         'country': 'philippines',
#         'population': 51_500_000,
#         'fact': 'their war flag was their flag downwards'
#     },
#     'new york': {
#         'country': 'usa',
#         'population': 2_441_500_000,
#         'fact': 'usa has most improved country'
#     }
# }
#
# for city, country in cities.items():
#     print(f"\nCapital    : {city.title()}")
#     print(f"Country    : {country['country']}\n"
#           f"Population : {country['population']}\n"
#           f"Fact       : {country['fact']}"

