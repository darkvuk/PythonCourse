# STRING LIST

animals = ['Dog', 'Cat', 'Elephant']

print(len(animals))

animals.append('Cow')
print(animals)

animals.remove('Dog')
print(animals)

print(animals[2])

del animals[1]
print(animals)

# extend(string) - novi element je unesen slovo po slovo u listi ili
# extend(lista) - dodaje se elementi nove liste na postojecu listu
# append(lista) - dodaje se cijela nova lista u postojecu listu
animals.extend('Fish')
animals.extend(['Mouse', 'Rat'])
print(animals)

# Jos jedan nacin dodavanja
animals += ['Kangaroo', 'Rabbit']
print(animals)

# Vise razlicitih tipova podataka moze biti u jednoj listi
animals.extend(10, 8.9)
print(animals)