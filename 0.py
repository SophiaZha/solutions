import itertools
import heapq
from collections import defaultdict, Counter

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