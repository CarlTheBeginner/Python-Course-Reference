# 1
#places = ['paris', 'wellington', 'new york', 'london', 'tokyo']
#print(places)

#print("\n")
#print(sorted(places))
#print(places)
#print(sorted(places, reverse=True))
#print(places)

#print("\n")
#places.reverse()
#print(places)
#places.reverse()
#print(places)

#print("\n")
#places.sort()
#print(places)
#places.sort(reverse=True)
#print(places)

# 3
# COUNTRIES DATA ENTRY
countries = []
countries.append('China')
countries.insert(0, 'Japan')
countries.insert(1, 'Indonesia')
countries.insert(2, 'Brazil')
countries.insert(3, 'England')

print(sorted(countries, reverse=True))
countries.sort()

countries.remove('China')
countries.pop()

countries.reverse()
print(countries)


print(len(countries))

print(F"{countries[0].upper()} is my favourite country")

countries.append('USA')
countries.append('Thailand')

print(countries)

print(f"you going to change your destination to {countries[-1].upper()} ")

# 4.
print(len(countries))
# print(countries[6])
