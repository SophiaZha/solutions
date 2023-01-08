from enum import Enum

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