# https://leetcode.com/problems/network-delay-time/
# https://www.youtube.com/watch?v=EaphyqKU4PQ
import collections
import heapq
def get_shortest_time(startNode, endNode, paths):
    routes = collections.defaultdict(list)
    for p in paths:
        routes[p[0]].append((int(p[2]), p[1]))
        heap = [(0, startNode)]
        visited = set()
        time_dict = {}
        time_dict[startNode] = 0
    while heap:
        curr_time, curr_loc = heapq.heappop(heap)
        if curr_loc not in visited:
            visited.add(curr_loc)
            if curr_loc == endNode:
                return curr_time
            for time, to_loc in routes.get(curr_loc, ()):
                if to_loc in visited:
                    continue
                prev = time_dict.get(to_loc, -1 )
                new_time = curr_time + time
                if prev == -1 or new_time < prev:
                    time_dict[to_loc] = new_time
                    heapq.heappush(heap, (new_time, to_loc))
    return 0
start = "S0"
end = "S4"
paths = [
    ["S0", "S1", 16 ],
    ["S0", "S2", 6],
    ["S1", "S3", 8],
    ["S2", "S3", 9],
    ["S2", "S4", 3],
    ["S1", "S4", 106],
    ["S3", "S4", 1]
]
print(get_shortest_time(start, end, paths))