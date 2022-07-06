graph = {'A': set([('B', 29), ('F', 10)]), 
        'B': set([('A', 29), ('C', 16), ('G', 15)]),    
        'C': set([('B', 16), ('D', 12)]),    
        'D': set([('C', 12), ('E', 22), ('G', 18)]),    
        'E': set([('D', 22), ('F', 27), ('G', 25)]),
        'F': set([('A', 10), ('E', 27)]),
        'G': set([('B', 15), ('D', 18), ('E', 25)]), }

def printAllEdges(graph):
    visited = {}
    result = True
    for v in graph:
        for e in graph[v]:

            if(v in visited):
                if(e[0] in visited[v] and e[1] in visited):
                    result = False

            if(result):
                print("(%s,%s,%d)" % (v, e[0],e[1]) , end="")
            else:
                visited.add()






printAllEdges(graph)

# graphAL = { …. }
# def weightSum(graph): # 가중치의 총 합을 구하는 함수
# def printAllEdges(graph):

# print('AL : weight sum = ', weightSum(graphAL))
# printAllEdges(graphAL)
