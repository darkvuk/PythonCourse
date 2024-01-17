# TRY / EXCEPT

try:
    i = 0
    j = 10 / i
    print('hey')            # do ovog dijela se nece doci ako je vec doslo do exceptiona
except:
    print('Exception')      # nece se doci do ovog dijela koda ako je i != 0
    j = 0

# da nema try / except, ne bi se doslo do ovog dijela koga
print(j)
print("END")