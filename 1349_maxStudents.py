import functools
import operator
from collections import defaultdict
from itertools import chain
from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        Q = True
        m, n = len(seats), len(seats[0])

        s, t = (m, 0), (m, 1)

        def adj(v):
            r, c = v
            if (r, c) == t:
                return
            if (r, c) == s:
                for nr in range(m):
                    for nc in range(0, n, 2):
                        if seats[nr][nc] == ".":
                            yield (nr, nc)
                return
            if not c & 1:
                for dr in (0, -1, 1):
                    for dc in (-1, 1):
                        nr, nc = r + dr, c + dc
                        if nr in range(m) and nc in range(n):
                            if seats[nr][nc] == ".":
                                yield nr, nc
            if c & 1:
                yield t

        def rev_adj(v):
            r, c = v
            if (r, c) == s:
                return
            if (r, c) == t:
                for nr in range(m):
                    for nc in range(1, n, 2):
                        if seats[nr][nc] == ".":
                            yield (nr, nc)
                return
            if c & 1:
                for dr in (0, -1, 1):
                    for dc in (-1, 1):
                        nr, nc = r + dr, c + dc
                        if nr in range(m) and nc in range(n):
                            if seats[nr][nc] == ".":
                                yield nr, nc
            if not c & 1:
                yield s

        cap = defaultdict(lambda: 1)

        rev_cap = defaultdict(int)
        flow = 0
        while True:
            q = [s]
            ps = {}
            seen = set([s])
            while q:
                v = q.pop()
                if v == t:
                    break
                for w in adj(v):
                    if not cap[v, w] or w in seen:
                        continue
                    ps[w] = v
                    seen.add(w)
                    q.append(w)
                for w in rev_adj(v):
                    if not rev_cap[v, w] or w in seen:
                        continue
                    ps[w] = v
                    seen.add(w)
                    q.append(w)
            if v != t:
                break
            flow += 1
            v = ps[t]
            cap[v, t] -= 1
            rev_cap[t, v] += 1
            pp = f"{t}"
            while v != s:
                if ps[v] == s or v == t or v[1] & 1:
                    cap[ps[v], v] -= 1
                    rev_cap[v, ps[v]] += 1
                else:
                    cap[v, ps[v]] += 1
                    rev_cap[ps[v], v] -= 1
                if not Q:
                    pp = f"{v} -> {pp}"
                v = ps[v]
            Q or print(pp)
        chairs = sum(1 for _ in filter(functools.partial(operator.eq, "."), chain(*seats)))
        return chairs - flow


"""
[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
[[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]
[["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]
[["#"]]
[["#"],["."],["."]]
[["#",".","."]]
[["#","#","#","#","#","#"],["#","#","#","#","#","#"],["#","#","#","#","#","#"],["#","#","#","#","#","#"],["#","#","#","#","#","#"],["#","#","#","#","#","#"]]
[[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."]]
[["#",".","#"],[".","#","#"],["#",".","#"]]
[[".",".","."]]
[[".",".",".",".",".",".","."]]
[[".",".","#",".",".",".","."]]
[["#",".","#",".",".",".","."]]
[["."]]
[["#","."]]
[[".",".",".","."],[".",".",".","."]]
[[".","#","#","."],[".",".",".","#"],[".",".",".","."],["#",".","#","#"]]
[[".","#","#","."],[".",".",".","#"],[".",".",".","."]]
[["#","#","#",".","#"],[".",".","#",".","."],["#",".","#",".","#"],[".",".",".",".","."],[".",".",".","#","."]]
[[".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".","."],[".",".","#",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","#",".",".","#","."]]
[[".",".",".",".",".",".",".","."],[".",".",".",".",".",".","#","."],[".",".","#",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
[[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
"""