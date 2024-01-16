# Return vrijednost


# Metoda koja stampa proizvod dva broja
def product_of_two_numbers(a, b):
    print(a * b)

product_of_two_numbers(5, 10)


# Metoda koja vraca proizvod dva broja
# Za prikazivanje vrijednosti treba koristiti print
def product_of_two_numbers(a, b):
    return a * b

product = product_of_two_numbers(5, 10)
print(product)

# Nad rezultatom funkcije se mogu raditi racunske operacije
product = product_of_two_numbers(6, 7)
product += 3
print(product)


# Metoda koja vraca sumu tri cijela broja
def sum_of_three_numbers(a, b, c):
    return a + b + c

result = sum_of_three_numbers(10, 20, 30)
print(result)


# Metoda koja racuna vrijednost treceg ugla ako su poznata dva ugla
# Zbir svih uglova u trouglu je 180
def calculate_third_angle(first, second):
    third = 180 - (first + second)
    return third

print(calculate_third_angle(45, 45))