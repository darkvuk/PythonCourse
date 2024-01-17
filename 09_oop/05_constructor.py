class Planet:
    def __init__(self, name='Earth'):
        self.name = name
        self.speed = 10

# Klasa moze da sadrzi samo jedan konstruktor
# Ako ih sadrzi vise, koristi se posljednji konstruktor

# Rjesenje: koriscenje default vrijednosti
planet1 = Planet()
planet2 = Planet('Jupiter')
print(planet1.name)
print(planet2.name)
print(planet1.speed)
print(planet2.speed)

