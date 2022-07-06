import collections as cols
import queue
from time import sleep

g1 = {"0": set(["1"]), 
      "1": set(["0", "2", "3"]), 
      "2": set(["1", "4"]), 
      "3": set(["1", "4", "5"]), 
      "4": set(["2", "3"]), 
      "5": set(["3", "6", "7"]), 
      "6": set(["5", "7"]),  
      "7": set(["8", "9"]), 
      "8": set(["7"]), 
      "9": set(["7"]),  }


def bfs(graph, start):
    visited = set([start])
    queue = cols.deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex,end="-")
        nbr = graph[vertex] - visited
        for v in nbr:
            visited.add(v)
            queue.append(v)

bfs(g1, "3")
print("\n")