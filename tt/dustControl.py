import sys
workers, streets = 0, 0
tasks = []
for i, line in enumerate(sys.stdin):
    input = line.split(" ")
    n, m = int(input[0]), int(input[1])
    if i == 0:
        workers, streets = n, m
        tasks = [0 for i in range(m + 1)]
    else:
        tasks[n] += 1
        tasks[m+1] -= 1

ret = 0
s = 0
for i in range(len(tasks) - 1):
    s += tasks[i]
    if s == 0:
        ret += 1
print(ret)



