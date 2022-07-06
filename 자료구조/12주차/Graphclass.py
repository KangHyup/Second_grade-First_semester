vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [[ 0,  1,  1,  0,  0,  0,  0,  0], 
          [ 1,  0,  0,  1,  0,  0,  0,  0], 
          [ 1,  0,  0,  1,  1,  0,  0,  0],
          [ 0,  1,  1,  0,  0,  1,  0,  0],
          [ 0,  0,  1,  0,  0,  0,  1,  1],
          [ 0,  0,  0,  1,  0,  0,  0,  0],
          [ 0,  0,  0,  0,  1,  0,  0,  1],
          [ 0,  0,  0,  0,  1,  0,  1,  0]]

def dfs(gragh, start, visited = set() ):
    if start not in visited:
        visited.add(start)
        print(start, end='')
        nbr = gragh[start] - visited
        for v in nbr:
            dfs(gragh, v, visited)