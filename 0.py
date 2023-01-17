import itertools
import heapq
from collections import defaultdict, Counter
import operator
import math
from collections import OrderedDict
numbers = [2, 4, 6, 8, 1]

for number in numbers:
    if number % 2 == 1:
        print(number)
        break
else:
    print("No odd numbers")
my_list = [1, 2, 3, 4, 5]
one, two, haha, four, five = my_list

print( haha)

scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]

print(heapq.nlargest(3, scores))  # [91, 87, 82]
print(heapq.nsmallest(5, scores))  # [15, 33, 33, 49, 51]

# creating a simple dict
my_dict = {'kiwi': 4, 'apple': 5, 'cat': 3}

# creating empty ordered dict
ordered_dict = OrderedDict()
print(ordered_dict)

# creating ordered dict from dict
ordered_dict = OrderedDict(my_dict)
print(ordered_dict)
# adding elements to dict
ordered_dict['dog'] = 3

# replacing a dict key value
ordered_dict['kiwi'] = 10
print(ordered_dict)

# removing and adding a value
ordered_dict.pop('kiwi')
print(ordered_dict)
ordered_dict['kiwi'] = 4
print(ordered_dict)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
print(x[0])
print(x[1])
print(x[2])

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print("txt find " + str(x))

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print("total occurance of x is: ", end = '')
print(x)

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
	print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
# A Python program to demonstrate working of key
# value change in OrderedDict
from collections import OrderedDict

print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
	print(key, value)

print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
	print(key, value)

for key, value in od.items():
	print(key, value)

# A Python program to demonstrate working of deletion
# re-insertion in OrderedDict
from collections import OrderedDict

print("Before deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
	print(key, value)

print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
	print(key, value)

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
	print(key, value)



print(Counter("mississippi"))
print("String as input   :",  end='')
print(Counter(list("mississippi")))
print("List as input     :",  end='')
print(Counter(i=4, s=4, p=2, m=1))
print("Set as input      :",  end='')
print(Counter(set("mississippi")))

sales = Counter(apple=25, orange=15, banana=12)
monday_sales = Counter(apple=10, orange=8, banana=3)
sales.update(monday_sales)
tuesday_sales = {"apple": 4, "orange": 7, "tomato": 4}
sales.update(tuesday_sales)
print(sales)


letters = Counter("mississippi")
letters["p"]
letters["s"]
for letter in letters:
    print(letter, letters[letter])
for letter in letters.keys():
    print(letter, letters[letter])
for count in letters.values():
    print(count)
for letter, count in letters.items():
    print(letter, count)

n = 10
k = 2
# Get the number of ways to choose k items from n items without repetition and without order
nCk = math.comb(n, k)
print(nCk)
n = 5
k = 3
# Get the number of ways to choose k items from n items without repetition and without order
nCk = math.comb(n, k)
print(nCk)
# https://docs.python.org/3/library/math.html#math.comb

class check:
    def __init__(self):
        print("Address of self = ", id(self))
obj = check()
print("Address of class object = ", id(obj))
obj2 = check()
print("Address of class object2 = ", id(obj2))
# https://www.geeksforgeeks.org/self-in-python-class/

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
x = car.get("xmodel")
print(x)
#print(car["xmodel"])   -- KeyError
x = car.get("xmodel", "default")
print(x)
x = car.setdefault("xmodel", "Bronco")
print(x)


dict_cities = {'Uganda': 763, 'France': 830, 'Tokyo': 193, 'Malaysia': 1682}
max_val = list(dict_cities.values())
max_ke = list(dict_cities.keys())
print("1: " + max_ke[max_val.index(max(max_val))])  #1: Malaysia
print("2: " + max(dict_cities, key= dict_cities.get))  #2: Malaysia

your_dictionary = {'Australia':1780, 'England':6723, 'Tokyo': 1946}
new_maximum_val = max(your_dictionary.keys(), key=(lambda new_k: your_dictionary[new_k]))
print("Maximum Value''s key ", new_maximum_val)   #England
print("Maximum Value''s key 2 ", max(your_dictionary, key=your_dictionary.get))  #England

print('Maximum Value: ',your_dictionary[new_maximum_val])  # 6723
new_minimum_val = min(your_dictionary.keys(), key=(lambda new_k: your_dictionary[new_k]))
print('Minimum Value: ',your_dictionary[new_minimum_val])   # 1780

my_dictionary = {'Micheal': {'i': 15, 'z': 14},
                 'George': {'q': 2, 'y': 10, 'w': 3},
                 'John': {'n': 19}}
new_out = {}
for new_k, new_v in my_dictionary.items():
    count_new = 0
    for element in new_v.values():
        if element > count_new:
            count_new = element
    new_out[new_k] = count_new
print("new out " + str(new_out))   # {'Micheal': 15, 'George': 10, 'John': 19}

new_out_again = {}
for new_k, new_v in my_dictionary.items():
    new_out_again[new_k] = max(new_v.values())
print("new out again " + str(new_out_again))   #{'Micheal': 15, 'George': 10, 'John': 19}

dict_new = {'Micheal': [17,27,81], 'Elijah': [19,61,92]}
new_val = max((max(dict_new[key]) for key in dict_new))
print("dict_new new_val " + str(new_val))   # 92

val_2 = max(dict_new[key] for key in dict_new)
print("the list with largest value: " + str(val_2))   #[19,61,92]  because 19 > 17
val_3 = min(dict_new[key] for key in dict_new)
print("the list with smallest value: " + str(val_3))   #[17, 27, 81]  because 19 > 17
val_4 = max(min(dict_new[key] for key in dict_new))
print("the list with smallest value overall, and get the largest: " + str(val_4))   # 81

alpha_dict = {"g": 14, "q": 16, "h": 19}
new_value = max(alpha_dict, key=alpha_dict.get)
print("Highest value from dictionary:",new_value)   # h

name_dict = {"Oliva": 18, "potter": 56, "Harry": 15}
new_val = name_dict.values()
maximum_val = max(new_val)
print("Maximum value from dict:",maximum_val)  #56

Country_dict = {'China':982, 'Egypt':758, 'Malaysia' : 12}
new_val = max(Country_dict, key= lambda x: Country_dict[x])
print("maximum value from Country_dict:",new_val)   #China
new_val = max(Country_dict, key=Country_dict.get)
print("maximum value from Country_dict 2 :",new_val)   #China

max_dict = {'Australia':178, 'Germany':213, 'Japan': 867}
new_ma_val = max(max_dict.items(), key=operator.itemgetter(1))[0]
print("use operator itemgetter  " + new_ma_val)

my_new_dict = {"q": 18, "z": 10, "o": 13}
fin_max = max(my_new_dict, key=my_new_dict.get)
print("my_new_dict Maximum value:",fin_max)   # q
# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
# using heapify() to convert list into heap
heapq.heapify(li1)
# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))
print("The largest numbers in list are : ", end="")
print(heapq.nlargest(1, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))

str1 = ""
some_list = ["Welcome ", "To ", "Bonus ", "Tips"]
print(str1.join(some_list))

a = [[1, 2], [3, 4], [5, 6]]
b = list(itertools.chain.from_iterable(a))
print(b)

a=[10,9,8,7]
print(a[::-1])
a=["a","b","c","d"]
b=["e","f","g","h", "k"]

for x, y in zip(a, b):
 print(x,y)
else:
 print(x,y)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a[-3:-1]

a = [1, 2, 3, 4, 2, 2, 3, 1, 2, 2, 2]
print(max(set(a)))
print(max(set(a), key = a.count))

a="Python is the language of the future"
b=a.split()
print(b)

print("on"*3+ " " + "off"*2)

def is_anagram(str1, str2):
   return Counter(str1) == Counter(str2)

print(is_anagram("taste", "state"))
print(is_anagram("beach", "peach"))
print(Counter("helloo"))

dict1={"a": 1, "b": 2,"c": 3,"d": 4,"e": 5,"f": 6, "g": 7}
dict2={v: k for k, v in dict1.items()}
print(dict2)

for a, b in dict1.items():
    print ( a + " " + str(b))

a = defaultdict(set)
print(a)

words =  [  "wrt",  "wrf",  "er",  "ett",  "rftt"]
adj = {char: set() for word in words for char in word}
print(adj)

words =  [  "wrt",  "wrf",  "er",  "ett",  "rftt"]
adj = {str: set() for str in words }
print(adj)

words =  [  "wrt",  "wrf",  "er",  "ett",  "rftt"]
in_degree = Counter({c: 0 for word in words for c in word})
print(in_degree)

arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]
counter = Counter(arr)
top_three = counter.most_common(3)
print(counter)
print("top three = " + str(top_three))


olded = defaultdict(list)
times = [[2,1,1],[2,3,1],[3,4,1]]
edges = {u: [] for u, v, w in times}
olded = defaultdict(list)
print(edges)
print(olded)

a = [[[i*i for i in range(3)] for j in range(4)] for m in range(2)]
[[[0, 1, 4], [0, 1, 4], [0, 1, 4], [0, 1, 4]],
 [[0, 1, 4], [0, 1, 4], [0, 1, 4], [0, 1, 4]]]

a = [[i*i for i in range(3)] for ajkdfjasdfjdsafjadsk in range(4)]
a = [[i for i in range(0)] for j in range(3)]
m = {i:[] for i in range(3)}
b = [[] for j in range(4)]
a = [1,2,3,4]
print(a)
x = a.pop(0)
print("x = " + str(x))
print(a)
a.insert(0,1)
print(a)
## https://www.turing.com/kb/22-hottest-python-tricksfor-efficient-coding
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
# Hi Joe!
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght" #The third parameter in the mapping table describes characters that you want to remove from the string:
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))
# G i Joe!
# define string
string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)

# print count
print("The count is:", count) #2 as there are 2 occurences
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
print(1, 2, 3, "a", "z", "this is here", "here is something else")

print("Hello", end="")
print("World")  # HelloWorld
print("Hello", end=" ")
print("World")  # Hello World
print('words',   'with', 'commas', 'in', 'between', sep='? ')
# words, with, commas, in, between