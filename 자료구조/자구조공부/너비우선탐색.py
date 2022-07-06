import collections


import collections as cols
import queue

def bfs(graph, start):
    visited = set([start])
    queue = cols.deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        nbr = graph[vertex] - visited
        for v in nbr:
            visited.add(v)
            visited.append(v)