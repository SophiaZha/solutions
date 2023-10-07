# Python code to swap key and value
# of dictionary using defaultdict
from collections import defaultdict
dict1 = {"a": 1, "b": 2, "c": 3, "d": 2}
dict2 = defaultdict(list)
{dict2[v].append(k) for k, v in dict1.items()}
print(dict(dict2))


dict2 = {}
for k, v in dict1.items():
    dict2[v] = dict2.get(v, []) + [k]
print(dict2)