# WHILE PETLJA

i = 1
while i <= 5:
    print(i)
    i += 1



# Stampaj kvadrate do odredjenog broja
def print_squares_upto_limit(n):
    i = 1
    while i ** 2 < 30:
        print(i ** 2)
        i += 1

print_squares_upto_limit(30)



# Stampaj kubove do odredjenog broja
def print_cubes_upto_limit(n):
    i = 1
    while i ** 3 < 30:
        print(i ** 3)
        i += 1

print_cubes_upto_limit(30)



"""
 Vjezba
 Korisnik unosi dva cijela broja i bira jednu od ponudjenih operacije:
 1 - sabiranje
 2 - oduzimanje
 3 - dijeljenje
 4 - mnozenje
 5 - izlaz
 Program stampa rjesenje
 
 PONAVLJA SE IZNOVA!
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
print("5 - izlaz")
op = int(input())
print()

while op != 5:
    if op == 1:
        print(x + y)
    elif op == 2:
        print(x - y)
    elif op == 3:
        print(x / y)
    elif op == 4:
        print(x * y)

    op = int(input())
    print()