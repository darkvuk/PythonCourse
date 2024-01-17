class Animal():
    def bark(self):
        print('bark')



animal = Animal()
animal.bark()


class Pet(Animal):
    def groom(self):
        print('groom')


pet = Pet()
pet.groom()
pet.bark()