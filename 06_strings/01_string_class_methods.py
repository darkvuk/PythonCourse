# METODE U STRING KLASI

message = "Hello World"


# upper - velika slova
# isupper
x = message.upper()
print(x)
print(x.isupper())


# lower - mala slova
# islower
x = message.lower()
print(x)
print(x.islower())


# capitalize - veliko pocetno slovo, ostala slova su mala
# istitle
x = message.capitalize()
print(x)
print('Hello'.istitle())


# isalpha - da li je string sastoji smo od slova (bez razmaka!)
print('darkov'.isalpha())

# isdigit - da li je string broj
print('154545'.isdigit())

# isalnum - da li se string broj ili rijec
print('darko160124'.isalnum())


# startswith - da li string pocinje s nekim substringom
# endswith - da li string zavrsava s nekim substringom
print('Hello World'.startswith('hell'))
print('Hello World'.endswith('orld'))


# find - od kog indeksa se prvi put pojavljuje neki substring
print('Hello World'.find('lo'))
