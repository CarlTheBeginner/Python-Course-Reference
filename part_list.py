# 1.
pizzas = ['hawaiian', 'napoli', 'new york', 'greek', 'tecathlon']

print(f"The first three items on the list are : {pizzas[0:3]}")
print(f"Three item from the middle of the list are : {pizzas[1:4]}")
print(f"The last three items on the list are : {pizzas[-3:]}")

# 2.
pizzas = ['hawaiian', 'napoli', 'new york', 'greek', 'vegetarian']

friends_pizzas = pizzas[:]
friends_pizzas.append('asian')

print(f"My favorite pizzas are: \n"
      f"{pizzas}")

print(f"My friends faavorite pizzas are \n"
      f"{friends_pizzas}")

# 3.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

friend_foods.append('ice cream')

for food in my_foods:
    print(food)

for friend in friend_foods:
    print(friend)