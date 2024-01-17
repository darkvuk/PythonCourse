class LandAnimal:
    def __init__(self):
        super().__init__()
        self.walking_speed = 5

    def increase_walking_speed(self, value):
        self.walking_speed += value


class WaterAnimal:
    def __init__(self):
        super().__init__()
        self.swimming_speed = 10

    def increase_swimming_speed(self, value):
        self.swimming_speed += value


# Amphibian nasljedjuje sve varijable i metode svojih super klasa
class Amphibian(WaterAnimal, LandAnimal):
    def __init__(self):
        super().__init__()


a = Amphibian()
a.increase_walking_speed(10)
print(a.walking_speed)