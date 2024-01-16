# FOR PETLJA

for i in range(1, 11):
    print(i)

for c in 'Hello World':
    print(c)

for w in 'Hello World'.split():
    print(w)

for item in [8, 7, 6]:
    print(item)



# Suma svih brojeva od 1 do n
def sum_upto_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(sum_upto_n(5))



# Da li je broj prost
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(1))



# Stampanje trougla brojeva
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
def print_a_number_triangle(n):
    for i in range (1, n+1):
        for j in range (1, i + 1):
            print(j, end=' ')
        print()

print_a_number_triangle(6)



# Suma djelilaca
def sum_of_divisors(n):
    sum = 0

    if n < 2:
        return sum

    for i in range(2, n):
        if(n % i == 0):
            sum += i

    return sum

print(sum_of_divisors(15))