from enum import Enum
import math
import ast
def check_if_anagram(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    return sorted(first_word) == sorted(second_word)

first_list = [1, 2, 3]
second_list = [1, 2, 3]

# Is their actual value the same?
print(first_list == second_list)  # True

# Are they pointing to the same object in memory
print(first_list is second_list)
# False, since they have same values, but in different objects in memory


third_list = first_list

print(third_list is first_list)
# True, since both point to the same object in memory

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string[0:5])  # This

#https://www.learnbyexample.org/python-string-slicing/
# Take three steps forward
# If S is a string, the expression S [ start : stop : step ] returns the portion of the string from index start to index stop, at a step size step.
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string[0:10:3])  # adgj
print(my_string[0:10:2])  # acegi
print(my_string[0:10:1])  # abcdefghij
print(my_string[::-1])
print(my_string[-7:-2])	# CDEFG

my_string = "This is just a sentence"
print(my_string[10:0:-1])  # suj si sih
# Take two steps forward
print(my_string[10:0:-2])  # sjs i

def string_to_list(string):
    return ast.literal_eval(string)

string = "[[1, 2, 3],[4, 5, 6]]"
my_list = string_to_list(string)
print(my_list)  # [[1, 2, 3], [4, 5, 6]]

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


groceries = ['milk', 'bread', 'tea']

new_groceries = sorted(groceries)
# new_groceries = ['bread', 'milk', 'tea']

print(new_groceries)

# groceries = ['milk', 'bread', 'tea']
print(groceries)

groceries.sort()

# groceries = ['bread', 'milk', 'tea']
print(groceries)
#98. You can check whether a value is not part of a list using “not in”
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = []

for i in range(9):
    if i not in odd_numbers:
        even_numbers.append(i)

print(even_numbers)  # [0, 2, 4, 6, 8]
print(ast)
# y = 90
# x = brighten_color(y)
# print("x after brighten color " + str(x) )
first_dictionary = {'name': 'Fatos', 'location': 'Munich'}
second_dictionary = {'name': 'Fatos', 'surname': 'Morina',
                     'location': 'Bavaria, Munich'}
result = first_dictionary | second_dictionary
print(result)
# {'name': 'Fatos', 'location': 'Bavaria, Munich', 'surname': 'Morina'}
print("29", "01", "2022", sep="/")  # 29/01/2022
print("name", "domain.com", sep="@")  # name@domain.com
my_list = ['a', 'b', 'c', 'd']

my_list.reverse()

print(my_list)  # ['d', 'c', 'b', 'a']
books = ('Atomic habits', 'Ego is the enemy', 'Outliers', 'Mastery')

print(books.index('Mastery'))   # 3
# 31
my_string = "abcdef"
print(my_string.startswith("b"))  # False

number = 1
print(id(number))  # 4325215472
print(id(1))  # 4325215472

number = 3
print(id(number))  # 4325215536
print(id(1))  # 4325215472
name = "Fatos"
print(id(name))  # 4422282544
name = "fatos"
print(id(name))  # 4422346608
my_tuple = (1, 2, 3, 4)
print(id(my_tuple))  # 4499290128

my_tuple = ('a', 'b')
print(id(my_tuple))  # 4498867584
cities = ["Munich", "Zurich", "London"]
print(id(cities))  # 4482699712

cities.append("Berlin")
print(id(cities))  # 4482699712
my_set = {1, 2, 3, 4}
print(id(my_set))  # 4352726176
my_set.add(5)
print(id(my_set))  # 4352726176
my_set = frozenset(['a', 'b', 'c', 'd'])
#my_set.add("a")
print("hello")
#38
print(check_if_anagram("testinG", "Testing"))  # True
print(check_if_anagram("Here", "Rehe"))  # True
print(check_if_anagram("Know", "Now"))  # False

#40
dictionary = {"a": 1, "b": 2, "c": 3}

keys = dictionary.keys()

print(list(keys))  # ['a', 'b', 'c']
dictionary = {"a": 1, "b": 2, "c": 3}

values = dictionary.values()

print(list(values))  # [1, 2, 3]

#42
dictionary = {"a": 1, "b": 2, "c": 3}

reversed_dictionary = {j: i for i, j in dictionary.items()}

print(reversed)  # {1: 'a', 2: 'b', 3: 'c'}
#43
print(int(False))  # 0
print(int(True))  # 0
print(float(True))  # 1.0
x = 10 #44
y = 12
result = (x - False)*(y * True)
print(result)  # 0.8333333333333334

print(bool(.0))  # False
print(bool(3))  # True
print(bool("-"))  # True
print(bool("string"))  # True
print(bool(" "))  # True
#47
my_list = [3, 4, 5]

my_list.append(6)
my_list.insert(0, 2)
print(my_list)  # [2, 3, 4, 5, 6]