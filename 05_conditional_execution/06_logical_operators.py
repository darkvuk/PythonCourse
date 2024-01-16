# Logicki operatori - OR, AND, NOT

# NOT
print(not True)         # False
print(not False)        # True
print()

# AND
print(True and False)   # False
print(False and True)   # False
print(True and True)    # True
print(False and False)  # False
print()

# OR
print(True or False)   # True
print(False or True)   # True
print(True or True)    # True
print(False or False)  # False
print()

# XOR
print(True ^ True)     # False
print(True ^ False)    # True
print(False ^ True)    # True
print(False ^ False)   # False
print()

#-------------------------------

# Numericke vrijednosti od True i False
print(int(True))       # 1
print(int(False))      # 0

# Svaki broj vraca True - samo 0 vraca False
print(bool(-9))
print(bool(0))
print()

#-------------------------------

i = 10
j = 15

if i % 2 == 0 and j % 2 == 0:
    print("Both numbers are even.")
elif i % 2 == 0 or j % 2 == 0:
    print("At least one number is even.")
else:
    print("Both numbers are odd.")