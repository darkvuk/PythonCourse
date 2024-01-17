# LIST SLICING

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Pristup jednom elementu
x = numbers[5]
print(5)

# Pristup vise elemenata
# [x, y)
x = numbers[2:6]
print(x)

# od pocetka do 6 - 1 = 5
x = numbers[:6]
print(x)

# od 3 do kraja liste
x = numbers[3:]
print(x)

# pocinje od 1 i onda uzima svaki drugi broj
x = numbers[1:8:2]
print(x)

x = numbers[1:8:3]
print(x)


x = numbers[::3]
print(x)

# obrnuta lista
x = numbers[::-1]
print(x)

# pocinje od posljednjeg elementa i onda uzima svaki treci element
x = numbers[::-3]
print(x)

# brisanje brojeva 5 i 6
del numbers[5:7]
print(numbers)

# dodavanje elemenata u odredjenom opsegu
numbers[5:7] = ['five', 'six']
print(numbers)