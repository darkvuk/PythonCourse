# LIST COMPREHENSION

numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']


numbers_length_four = []
for number in numbers:
    if len(number) == 4:
        numbers_length_four.append(number)
print(numbers_length_four)


number_lengths = [len(number) for number in numbers]
print(number_lengths)


numbers_upper = [number.upper() for number in numbers]
print(numbers_upper)


numbers_length_four = [number for number in numbers if len(number) == 4]
print(numbers_length_four)


list = [3, 6, 9, 1, 4, 15, 6, 3]
list_odd = [number for number in list if number % 2 == 1]
print(list_odd)
