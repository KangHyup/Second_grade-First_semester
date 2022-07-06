
class ArrayList:
    def __init__( self ):
        self.items = []

    def insert(self, pos, elem) :
        self.items.insert(pos, elem)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty( self ):
        return self.size() == 0
    def getEntry(self, pos) :
        return self.items[pos]
    def size( self ):
        return len(self.items)
    def clear( self ) :
        self.items = []
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[pos] = elem

    #삽입정렬
    def sort(self) :
        n = len(self.items)
        for i in range(1, n) :
            key = self.items[i]
            j = i-1
            while j>=0 and self.items[j] > key :
                self.items[j + 1] = self.items[j]
                j -= 1
            self.items[j + 1] = key
        
    def merge(self, lst) :
        self.items.extend(lst)
    def display(self, msg='ArrayList:' ):
        print(msg, self.size(), self.items)

