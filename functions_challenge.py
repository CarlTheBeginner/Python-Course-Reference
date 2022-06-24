# 1
# def message():
#     print("I've learned about loops while and functions")
#
# message()

# 2
# def favorite_book(title):
#     print(f"One of my favorite books is {title.title()}")
#
# favorite_book('atomic habits')

# 3
# def make_shirt(text, size):
# #     print(f"The size of the shirt is {size}, :{text}")
# #
# # make_shirt('adidas', 15)
# # make_shirt(text='rrj', size=19)


# 4
# def make_shirt(text, size='large', default='i love python'):
#     print(f"The size of the shirt is {size}, :{text}\n"
#           f"{default}")
#
# make_shirt('adidas')
# make_shirt(text='rrj')
# make_shirt('tribal', size='medium')

# 5
# def describe_country(city, country='iceland'):
#     print(f"{city.title()} is in {country.title()}")
#
# describe_country('manila', 'philippines')
# describe_country('new york', 'usa')
# describe_country('reykjavik')

# 6
# def city_country(city, country):
#     city_name = f"{city}, {country}"
#     return city_name.title()
#
# country = city_country('santiago', 'chile')
# country2 = city_country('manila', 'philippines')
# country3 = city_country('new york', 'usa')
#
# print(country + "\n",
#       country2 + "\n",
#       country3)


# 7
# def make_album(name, title, number_of_songs=None):
#     if number_of_songs:
#         album = {'artist_name': name, "album_title": title, 'number of songs': number_of_songs}
#     else:
#         album = {'artist_name': name, "album_title": title}
#     return album
#
# album = make_album('eminem', 'music to be murdered by', number_of_songs=17)
# album2 = make_album('eminem', 'kamikaze')
# album3 = make_album('eminem', 'marshall mathers lp2')
# print(album)
# print(album2)
# print(album3)


# 8
# def make_album(name, title):
#         album = {}
#         album['artist_name'] = name
#         album['album_title'] = title
#         return album
#
# while True:
#     name = input("\nPlease enter the music artist: ")
#     print("Press 'q' anytime if you want to quit")
#     if name == 'q':
#         break
#
#     album_name = input("Please enter his album: ")
#     if album_name == 'q':
#         break
#
#     full_album = make_album(name, album_name)
#     print(dict(full_album))

# 9
# def show_messages(messages):
#     for message in messages:
#         print(message)
#
#
# messages = ['hi im chucky', 'lorem mamaa mo ', 'omg bruh oh hell no man', 'make my day in beaches', 'sons of anarchy']
# show_messages(messages)

# 10 - 11
# def send_messages(messages, sent_messages):
#     while messages:
#         sending_messages = messages.pop()
#
#         print(f"Sending messages: {sending_messages}")
#         sent_messages.append(sending_messages)
#
# def sent_messages(sent_messages):
#     print(f"The following messages are sent: ")
#     for sent_message in sent_messages:
#         print(f"\t - {sent_message}")
#
# message = ['hi im chucky', 'lorem mamaa mo ', 'omg bruh oh hell no man', 'make my day in beaches', 'sons of anarchy']
# sent_message = []
#
#
# send_messages(message[:], sent_message)
# sent_messages(sent_message)
# print(message)
# print(sent_message)

# 12
# TODO Sandwiches: Write a function that accepts a list of items a person wants
#      on a sandwich. The function should have one parameter that collects as many
#      items as the function call provides, and it should print a summary of the
#      sandwich that’s being ordered.Call the function three times, using a
#      different number of arguments each time.

# def sandwiches(*type_sandwiches):
#     print("What i want on my sandwich is : ")
#     for type_sandwich in type_sandwiches:
#         print(f"\t- {type_sandwich}")
#
# sandwiches('cheese')
# sandwiches('cheese', 'bacon', 'egg')
# sandwiches('ham', 'salami', 'pastrami')

# 13
# def build_profile(first, last, **user_info):
#         """Build a dictionary containing everything we know about a user."""
#         user_info['first_name'] = first.title()
#         user_info['last_name'] = last.title()
#
#         return user_info
# user_profile = build_profile('carl', 'ballenas',
#                             age=21,
#                             course='BSIT')
#
# print(user_profile)

# 14
# def make_car(manufacturer, model_name, **other_info):
#     other_info['manufacturer'] = manufacturer
#     other_info['model'] = model_name
#     return other_info
#
# car_profile = make_car('subaru', 'outback', color='blue', tow_package=True, price=1499)
# print(car_profile)

