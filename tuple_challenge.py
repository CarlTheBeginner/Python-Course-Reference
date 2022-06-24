buffet = ('adobo', 'sinigang', 'bicol express', 'fried chicken', 'tinola')
for buff in buffet:
    print(buff)

change_menu = list(buffet)
change_menu[0] = 'chick fila'
change_menu[1] = 'raisin cane'

new_menu = tuple(change_menu)
print(new_menu)