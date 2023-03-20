import sys
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
#48. Lambda functions can only be in one line
#comparison = lambda x: if x > 3:
#   print("x > 3")
#                else:
#                    print("x is not greater than 3")
#
##
comparison = lambda x: "x > 3" if x > 3 else False
print(bool(comparison))
#51 map() returns a new object
my_list = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, my_list)

print(list(squared))   # [1, 4, 9, 16]
print(my_list)  # [1, 2, 3, 4]
for number in range(1, 10, 3):
    print(number, end=" ")
# 1 4 7
# 54. You don’t need to compare the length with 0
def get_element_with_comparison(my_list):
    if len(my_list) > 0:
        return my_list[0]


def get_first_element(my_list):
    if len(my_list):
        return my_list[0]


elements = [1, 2, 3, 4]
first_result = get_element_with_comparison(elements)
second_result = get_element_with_comparison(elements)

print(first_result == second_result)  # True

class Engineer:
    def __init__(self, name):
        self.name = name
        self.__starting_salary = 62000
#56. You can access private properties even outside their intended scope
dain = Engineer('Dain')
print(dain._Engineer__starting_salary)  # 62000
#57. Check the memory usage of an object
print(sys.getsizeof("bitcoin"))  # 56

def get_sum(*arguments):
    result = 0
    for i in arguments:
        result += i
    return result
#58. You can define a method that can be called with as many parameters as you want
#59. call parent class initializer usering super()
print(get_sum(1, 2, 3))  # 6
print(get_sum(1, 2, 3, 4, 5))  # 15
print(get_sum(1, 2, 3, 4, 5, 6, 7))  # 28
class Parent:
    def __init__(self, city, address):
        self.city = city
        self.address = address


class Child(Parent):
    def __init__(self, city, address, university):
        super().__init__(city, address)
        self.university = university


child = Child('Zürich', 'Rämistrasse 101', 'ETH Zürich')
print(child.university)  # ETH Zürich

class Expenses:
    def __init__(self, rent, groceries):
        self.rent = rent
        self.groceries = groceries

    def __add__(self, other):
        return Expenses(self.rent + other.rent,
                        self.groceries + other.groceries)


april_expenses = Expenses(1000, 200)
may_expenses = Expenses(1000, 300)

total_expenses = april_expenses + may_expenses
print(total_expenses.rent)  # 2000
print(total_expenses.groceries)  # 500
#61. You can also redefine the “<” and “==” operators inside your own classes
class Game:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score


first = Game(1)
second = Game(2)
#63. class equal
print(first < second)  # True
class Journey:
    def __init__(self, location, destination, duration):
        self.location = location
        self.destination = destination
        self.duration = duration

    def __eq__(self, other):
        return ((self.location == other.location) and
                (self.destination == other.destination) and
                (self.duration == other.duration))


first = Journey('Location A', 'Destination A', '30min')
second = Journey('Location B', 'Destination B', '30min')

print(first == second)
#62. define print object
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return repr('Rectangle with area=' + str(self.a * self.b))


print(Rectangle(3, 4))  # 'Rectangle with area=12'
#64. swap case
string = "This is just a sentence."
result = string.swapcase()
print(result)  # tHIS IS JUST A SENTENCE.
#65. check is space
string = "  "
result = string.isspace()
print(result)  # True
#65. isalphanumeric
name = "Password"
print(name.isalnum())  # True, because all characters are alphabets
name = "Secure Password "
print(name.isalnum())  # False, because it contains whitespaces
name = "S3cur3P4ssw0rd"
print(name.isalnum())  # True
name = "133"
print(name.isalnum())  # True, because all characters are numbers

#67. remove right based characters
string = "This is a sentence with       "
# Remove trailing spaces from the right
print(string.rstrip())  # "This is a sentence with"
print(string.rstrip("h "))  # "This is a sentence with"
string = "this here is a sentence..,,,,aaaaasd"
print(string.rstrip(",dsace."))  # "this here is a sentence"
#68. Check if a string represents a number
string = "seven"
print(string.isdigit())  # False
string = "1337"
print(string.isdigit())  # True
string = "5a"
print(string.isdigit())  # False, because it contains the character 'a'
string = "2**5"
print(string.isdigit())  # False

#70. is Title
string = "This is a sentence"
print(string.istitle())  # False

string = "10 Python Tips"
print(string.istitle())  # True

string = "How to Print A String in Python"
# False, because of the first characters being lowercase in "to" and "in"
print(string.istitle())

string = "PYTHON"
print(string.istitle())  # False. It's titlelized version is "Python"

numbers = (1, 2, 3, 4)

print(numbers[-1])  # 4
print(numbers[-4])  # 1
#72. Nest a list and a tuple inside a tuple
mixed_tuple = (("a"*10, 3, 4), ['first', 'second', 'third'])

print(mixed_tuple[1])  # ['first', 'second', 'third']
print(mixed_tuple[0])  # ('aaaaaaaaaa', 3, 4)
#73. Quickly count the number of times an element appears in a list that satisfies a condition
names = ["Besim", "Albert", "Besim", "Fisnik", "Meriton"]
print(names.count("Besim"))  # 2
#74. You can easily get the last n elements using slice()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slicing = slice(-4, None)
# Getting the last 3 elements from the list
print(my_list[slicing])  # [7,8,9,10]
# Getting only the third element starting from the right
print(my_list[-3])  # 8




string = "Data Science"
# start = 1, stop = None (don't stop anywhere), step = 1
# contains 1, 3 and 5 indices
slice_object = slice(5, None)
print(string[slice_object])   # Science

# Initialize list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Show original list
print("\nOriginal List:\n", List)
print("\nSliced Lists: ")
# Display sliced list
print(List[3:9:2])
# Display sliced list
print(List[::2])
# Display sliced list
print(List[::])
print(List[::-1])
print(List[::-3])
print(List[9:4:-2])
print(List[:1:-2])
print(List[:0:-2])

my_tuple = ('a', 1, 'f', 'a', 5, 'a')
print(my_tuple.count('a'))  # 3
#76. index of element at tuple
my_tuple = ('a', 1, 'f', 'a', 5, 'a')
print(my_tuple.index('f'))  #  2

#77. subtuples making jumps
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple[::3])  # (1, 4, 7, 10)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple[3:])  # (4, 5, 6, 7, 8, 9, 10)

#79. remove all elments
my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)  # []

my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # set()

my_dict = {"a": 1, "b": 2}
my_dict.clear()
print(my_dict)  # {}

#80. join 2 sets
first_set = {4, 5, 6}
second_set = {1, 2, 3}

print(first_set.union(second_set))  # {1, 2, 3, 4, 5, 6}
first_set = {1, 2, 3}
second_set = {4, 5, 6}

first_set.update(second_set)

print(first_set)  # {1, 2, 3, 4, 5, 6}

def is_positive(number):
    print("Positive" if number > 0 else "Negative")  # Positive

is_positive(-3)