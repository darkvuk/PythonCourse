class MotorBike:
    def __init__(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def increase_speed(self, value):
        self.speed += value

    def decrease_speed(self, value):
        self.speed -= value

    def remove_speed(self):
        self.decrease_speed(self.speed)


honda = MotorBike(150)
print(honda.get_speed())

honda.increase_speed(200)
print(honda.get_speed())

honda.decrease_speed(100)
print(honda.get_speed())

honda.remove_speed()
print(honda.get_speed())