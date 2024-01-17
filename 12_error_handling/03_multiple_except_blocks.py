# VISE EXCEPT BLOKOVA

try:
    i = 0
    j = 10 / i
    numbers = [1, '2']
    print(sum(numbers))
    print('hey')            # do ovog dijela se nece doci ako je vec doslo do exceptiona
except TypeError:
    print('TypeError')
    j = 10
except ZeroDivisionError:
    print('ZeroDivisionError')
    j = 0

# da nema try / except, ne bi se doslo do ovog dijela koda
print(j)
print("END")


#---------------------------------------------------------------

# vise errora se hendluje sa istom porukom

try:
    sum([1, '2'])
except (ZeroDivisionError, TypeError) as error:
    print(error)

#--------------------------------------------------------------

# Dijeljenje sa nulom ce raditi i sa npr. ArithmeticError
# jer je ZeroDivisionError ispod njega u hijerarhiji

try:
    2 / 0
except ArithmeticError as error:
    print(error)

