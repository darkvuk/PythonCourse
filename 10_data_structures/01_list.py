# LISTA

marks = [45, 54, 80]

# sum - suma svih elemenata
x = sum(marks)
print(x)

# len - duzina liste
x = len(marks)
print(x)

# max - najveci element u listi
x = max(marks)
print(x)

# min - najmanji element u listi
x = min(marks)
print(x)

# append - dodaje element na kraj liste
marks.append(98)
print(marks)

# insert (pozicija, element) - dodaje element na odredjenoj poziciji
marks.insert(2, 54)
print(marks)

# Da li se element nalazi u listi
print(98 in marks)

# index - vraca indeks prvog pojavljivanja nekog elementa u listi
x = marks.index(54)
print(x)

# obilazak elemenata liste
for m in marks:
    print(m)

# obilazak elemenata liste (uz indekse)
for i, m in enumerate(marks):
    print(f'{i} - {m}')