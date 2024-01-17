numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

# reverse - okrece listu
numbers.reverse()
print(numbers)
numbers.reverse()

# Upotreba reverse u for petlji
for number in reversed(numbers):
    print(number)

# Sortiranje u rastucem redoslijedu
numbers.sort()
print(numbers)
numbers.sort()

for number in sorted(numbers):
    print(number)

# Sortiranje po duzini stringa (opadajuci redoslijed)
numbers.sort(key=len, reverse=True)
print(numbers)