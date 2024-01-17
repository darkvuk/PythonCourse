# Rjecnik
# parovi kljuc : vrijednost

ponavljanje = dict(a=5, b=6, c=8)
print(ponavljanje)

# dodavanje u rjecnik
ponavljanje['d'] = 15
print(ponavljanje)

# azuriranje vrijednosti
ponavljanje['d'] = 10
print(ponavljanje)

# brisanje vrijednosti
del ponavljanje['d']
print(ponavljanje)

# dobijanje vrijednosti
x = ponavljanje.get('d')
print(x)

# svi kljucevi
x = ponavljanje.keys()
print(x)

# sve vrijednosti
x = ponavljanje.values()
print(x)

# parovi kljuc : vrijednost
x = ponavljanje.items()
print(x)

# prolazak kroz rjecnik for petljom
for key, val in ponavljanje.items():
    print(f'{key} : {val}')

#--------------------------------------

str = 'This is an awesome occasion. This has never happened before.'
print()

# Koliko puta se svaki karakter pojavljuje u stringu
ponavljanje = {}
for c in str:
    ponavljanje[c] = ponavljanje.get(c, 0) + 1
print(ponavljanje)

# Koliko puta se svaka rijec pojavljuje u stringu
ponavljanje = {}
for w in str.replace('.','').split(' '):
    ponavljanje[w] = ponavljanje.get(w, 0) + 1
print(ponavljanje)



# dictionary comprehension
squares = {i : i ** 2 for i in range(1,11)}
print(squares)