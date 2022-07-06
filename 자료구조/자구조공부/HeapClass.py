
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self): return len(self.heap)-1
    def isEmpty(self): return len(self.heap) == 0
    def Parent(self,i): return self.heap[i//2]
    def Left(self, i): return self.heap[i*2]
    def Right(self, i): return self.heap[i*2+1]
    def display(self, msg="힙트리: "):
        print(msg, self.heap[1:])
    
    def insert(self, n):
        self.heap.append(n)
        i=self.size()
        while( i != 1 and n > self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n

    #삭제연산: 제일 위의값을 죽이고, 말단을 사장자리에 놓음
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]            #삭제할 노드를 keep
            last = self.heap[self.size()]   #last = 말단 노드
            while(child <= self.size()):
                #왼쪽노드 < 오른쪽노드이면 오른쪽을 자리바꿀 후보로 놓음
                if child<self.size() and self.Left(parent) < self.Right(parent):
                    child+=1
                if last >= self.heap[child]: #말단이 자식보다 크기가 크다면 거기가 제자리
                    break;
                self.heap[parent] = self.heap[child] #break를 못했다면(자식이 말단보다 크다면) 부모자리를 자식에게 내어줌
                # 자식노드로 좌표를 바꿈
                parent = child
                child *= 2;

        self.heap[parent] = last
        self.heap.pop(-1)
        return hroot


heap = MaxHeap()
heap.insert(9); heap.insert(3); heap.insert(1); heap.insert(7); heap.insert(6); heap.insert(8)
heap.display()