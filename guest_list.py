# 1
guest_list = ['Jim', 'Michael', 'Dwight']
print(f"{guest_list[0]} welcome to dinner")
print(F"{guest_list[1]} welcome to dinner")
print(f"{guest_list[2]} welcome to dinner")
print(len(guest_list))
print()
# 2
removed_guest = guest_list.pop(2)
print(guest_list)
print(f"{removed_guest} was not able to go in restaurant")

guest_list.insert(2, 'Andy')
print(guest_list)
print(len(guest_list))

print(f"{guest_list[0]} welcome to dinner \n"
      f"{guest_list[1]} welcome to dinner \n"
      f"{guest_list[2]} welcome to dinner \n")

# 3
print("I found bigger dinner table.")
guest_list.insert(0, 'Pam')
guest_list.insert(2, 'Creed')
guest_list.append('Stanley')

print(guest_list)
print(len(guest_list))

# 4
print("i can invite 2 people only in my dinner....☺")
popped_list = [guest_list.pop(), guest_list.pop(), guest_list.pop(), guest_list.pop()]
print(popped_list)
print(guest_list)
print(len(guest_list))
