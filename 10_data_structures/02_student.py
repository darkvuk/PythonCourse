class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_number_of_marks(self):
        return len(self.marks)

    def get_total_sum_of_marks(self):
        return sum(self.marks)

    def get_max_mark(self):
        return max(self.marks)

    def get_min_mark(self):
        return min(self.marks)

    def get_avg_mark(self):
        return sum(self.marks) / len(self.marks)

    def add_new_mark(self, mark):
        self.marks.append(mark)

    def remove_mark_at_index(self, index):
        del self.marks[index]

    def get_marks(self):
        return self.marks


s1 = Student('Darko', [98, 67, 90, 54])
print(s1.get_marks())

s1.add_new_mark(20)
print(s1.get_marks())

s1.remove_mark_at_index(4)
print(s1.get_marks())

x = s1.get_max_mark()
print(x)

x = s1.get_min_mark()
print(x)

x = s1.get_avg_mark()
print(x)

x = s1.get_number_of_marks()
print(x)

x = s1.get_total_sum_of_marks()
print(x)