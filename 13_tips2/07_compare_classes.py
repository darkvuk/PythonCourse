class Student:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

s1 = Student(1)
s2 = Student(2)
s3 = Student(1)

print(s1 is s2)

# = - operator dodjele
s1 = s2
print(s1 is s2)

# == - poredjenje
s1 == s3
print(s1 == s2)