class MotorBike:
    def __init__(self, speed):
        self.speed = speed
        print('MotorBike instance created.')

honda = MotorBike(150)
ducati = MotorBike(250)

print(honda.speed)
print(ducati.speed)