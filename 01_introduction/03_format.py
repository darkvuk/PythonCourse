# Format

# 0 uzima prvu predatu vrijednost
print("VALUE {0}".format(5 * 2))
print("VALUE {0}".format(10, 20, 30))

# 1 uzima drugu predatu vrijednost
print("VALUE {1}".format(10, 20, 30))

# 2 uzima trecu predatu vrijednost
print("5 * 6 = {2}".format(5, 6, 5 * 6))

# Uzimanje vrijednosti vise argumenata
print("{0} * {1} = {2}".format(5, 6, 5 * 6))
print("{0} * {1} = {2}".format(5, 7, 5 * 7))

# Ne moraju svi argumenti da budu iskorisceni
# Ne smije biti manje argumenata
print("{0} * {1} = {4}".format(5, 8, 5 * 8, 5 * 9, 5 * 10))

# Floating point vrijednost kao argument
print("{0} * {1} = {2}".format(2.5, 2, 2.5 * 2))

# String kao argument
print("My name is {1}".format("Ranga", "Raja"))

# Drugi nacin formatiranja stringova je f""
a, b, c = 1, 2, 3
print(f"{a} + {b} + {c} = {a + b + c}")