from enum import Enum
import math
my_list = [1, 2, 3, 4]
print(my_list)  # [1, 2, 3, 4]
print(*my_list)  # 1 2 3 4
def sum_of_elements(*arg):
    total = 0
    for i in arg:
        total += i
    return total

result = sum_of_elements(*[1, 2, 3, 4])
print(result)  # 10

#5. Get all the elements in the middle of the list
_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]
print(elements_in_the_middle)  # [2, 3, 4, 5, 6, 7]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8]

class Status(Enum):
    NO_STATUS = -1
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2


print(Status.IN_PROGRESS.name)  # IN_PROGRESS
print(Status.COMPLETED.value)  # 2
string = "Abc"

print(string * 5)  # AbcAbcAbcAbcAbc
#11. Merge dictionaries in a single readable line
first_dictionary = {'name': 'Fatos', 'location': 'Munich', 'name': 'lei'}
second_dictionary = {'name': 'Fatos', 'surname': 'Morina',
                     'location': 'Bavaria, Munich'}
result = first_dictionary | second_dictionary
print(result)
# {'name': 'Fatos', 'location': 'Bavaria, Munich', 'surname': 'Morina'}

#12 Find the index of an element in a tuple
books = ('Atomic habits', 'Ego is the enemy', 'Outliers', 'Mastery')
print(books.index('Mastery'))   # 3
print(books.index('Outliers'))   # 3
list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num)
list_num[2] = 5
print(list_num)

print(tup_num[2])
print(dir(list_num))
print(dir(tup_num))

print(math.floor(math.log2(78)))

def subtract(a, b):
    return a - b
print((subtract(a=1, b=3)))  # -2
print((subtract(b=3, a=1)))  # -2

print(1_000_000_000)  # 1000000000
print(1_234_567)  # 1234567
print("9", "01", "2022", sep="/")  # 29/01/2022
print("name", "domain.com", sep="@")  # name@domain.com