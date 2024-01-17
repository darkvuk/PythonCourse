def method_1():
    print('Obicna metoda')

class ClassA:
    def class_method_1(self):
        print('Metoda klase')

if __name__ == '__main__':
    method_1()
    ClassA().class_method_1()