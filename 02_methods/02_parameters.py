# Metode sa parametrima


# Metoda koja stampa "Hello World" odredjen broj puta
def print_hello_world(no_of_times):
    for i in range(1, no_of_times + 1):
        print("Hello World")

print_hello_world(5)
print()


# Metoda koja stampa sve brojeve od 1 do n, ukljucujuci i 1 i n
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(15)
print()


# Metoda koja stampa kvadrate svih brojeva od 1 do n, ukljucujuci i 1 i n
def print_squares_of_numbers(n):
    for i in range(1, n + 1):
        print(i ** 2)

print_squares_of_numbers(15)
print()


# Metoda koja stampa neku recenicu n puta
def print_string(str, n):
    for i in range(1, n + 1):
        print(str)

print_string("Hello World", 2)
print()


# Metoda koja stampa neku recenicu n puta (sa deafult parametrima)
# Kad se ne predaju vrijednosti, funkcija ce uzeti default vrijednosti
# Kad se predaju vrijednosti, funkcija ce uzeti predate vrijednosti
def print_string(str = "Hello World", n = 2):
    for i in range(1, n + 1):
        print(str)

print_string()
print_string("Hi", 5)
print()

# Moze se i predati samo jedan argument bez obzira gdje je definisan u funkciji
print_string("Darko")
print_string(n = 10)
print()

# Broj se automatski pretvara u string
print_string(10)        # bez "n =", dva puta ce se stampati broj 10
print()

# Metoda koja kreira tablicu mnozenja za odredjeni broj
def print_multiplication_table(table):
    for i in range(1, 11):
        print(f"{table} * {i} = {table * i}")

print_multiplication_table(7)
print()

# Metoda koja kreira tablicu mnozenja za odredjeni broj (izmedju dva broja)
def print_multiplication_table2(table, start, end):
    for i in range(start, end + 1):
        print(f"{table} * {i} = {table * i}")

print_multiplication_table2(7, 1, 6)
print()