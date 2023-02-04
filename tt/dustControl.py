import sys
workers, streets = 0, 0
jobs = []
for i, line in enumerate(sys.stdin):
    input = line.split(" ")
    n, m = int(input[0]), int(input[1])
    if i == 0:
        workers, streets = n, m
        jobs = [0 for i in range(m + 1)]
    else:
        jobs[n] += 1
        jobs[m + 1] -= 1

ret = 0
s = 0
for i in range(len(jobs) - 1):
    s += jobs[i]
    if s == 0:
        ret += 1
print(ret)



