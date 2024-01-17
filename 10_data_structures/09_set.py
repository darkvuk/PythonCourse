# SKUP
# nema duplikate
# ne dozvoljava pristup preko indeksa


numbers = [1, 2, 55, 4]
print(numbers)

# pretvaranje u skup
numbers = set(numbers)
print(numbers)

# dodavanje
numbers.add(0)
print(numbers)

# uklanjanje
numbers.remove(0)
print(numbers)

# funkcije
print(min(numbers))
print(max(numbers))
print(len(numbers))
print(sum(numbers))

# kreiranje skupa pomocu range
set1 = set(range(1,6))
print(set1)

# unija
x = numbers | set1
print(x)

# presjek
x = numbers & set1
print(x)

# razlika
x = numbers - set1
print(x)

# set comprehension
squares = set(i ** 2 for i in range(1,11))
print(squares)