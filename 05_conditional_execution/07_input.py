# Input vrijednost

# Svaka input vrijednost bice string
x = input("Unesi broj: ")
print(type(x))

# String treba prebaciti u broj
x = int(input("Unesi broj: "))
print(type(x))

#-----------------------------------------

"""
 Vjezba
 Korisnik unosi dva cijela broja i bira jednu od ponudjenih operacije:
 1 - sabiranje
 2 - oduzimanje
 3 - dijeljenje
 4 - mnozenje
 Program stampa rjesenje
"""

x = int(input("Unesi prvi broj: "))
print()

y = int(input("Unesi drugi broj: "))
print()

print("Unesi operaciju: ")
print("1 - sabiranje")
print("2 - oduzimanje")
print("3 - dijeljenje")
print("4 - mnozenje")
op = int(input())
print()

if op == 1:
    print(x + y)
elif op == 2:
    print(x - y)
elif op == 3:
    print(x / y)
elif op == 4:
    print(x * y)
else:
    print("Izabrana operacija ne postoji.")