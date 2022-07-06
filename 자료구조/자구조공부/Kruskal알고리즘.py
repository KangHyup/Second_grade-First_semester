
##union-find함수: 사이클이 있는지 확인
#집합의 초기화함수

set_size = 0
parent = []
def init_set(nSets):
    global set_size, parent
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)

def find(id):
    while(parent[id] >= 0 ):
        id = parent[id]
    return id;

def union(s1, s2):
    global set_size
    parent[s1] = s2
    set_size = set_size-1

def MSTKruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = []

    for i in range(vsize-1):        #모든 간선을 리스트에 넣음
        for j in range(i+1, vsize):
            if adj[i][j] != None:
                eList.append( (i,j,adj[i][j]))

    #간선리스트의 가중치를 내림차순으로 정렬
    eList.sort(key = lambda e: e[2], reverse=True)

    edgeAccepted = 0
    while(edgeAccepted < vsize-1):
        e = eList.pop(-1)
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset:
            print("간선추가: (%s,%s,%d)" %(vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)
            edgeAccepted +=1



vertex = ['A','B','C', 'D', 'E', 'F', 'G' ]
weight = [[None, 29, None, None, None, 10, None], 
          [29, None, 16, None, None, None, 15], 
          [None, 16, None, 12, None, None, None], 
          [None, None, 12, None, 22, None, 18], 
          [None, None, None, 22, None, 27, 25], 
          [10, None, None, None, 27, None, None],
          [None, 15, None, 18, 25, None, None]]

MSTKruskal(vertex, weight)

