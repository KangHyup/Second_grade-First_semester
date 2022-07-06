class MinHeap:
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
        while( i != 1 and n < self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i//2
        self.heap[i] = n

    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]            
            last = self.heap[self.size()]   
            while(child <= self.size()):
                if child>self.size() and self.Left(parent) > self.Right(parent):
                    child+=1
                if last <= self.heap[child]: 
                    self.heap[parent] = self.heap[child]
                parent = child
                child *= 2;

        self.heap[parent] = last
        self.heap.pop(-1)
        return hroot

heap = MinHeap()
heap.insert(9); heap.insert(3); heap.insert(1); heap.insert(7); heap.insert(6); heap.insert(8)
heap.display()
