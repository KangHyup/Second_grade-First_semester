
class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value
    def __str__( self ):
        return str("%s:%s"%(self.key, self.value) )

class BinaryMap:
    def __init__( self ):
        self.table = []

    def display(self, msg):
        print(msg)
        for entry in self.table :
            print(" ", entry)
    
    def delete(self, key) :
        for i in range(self.size()):
            if self.table[i].key == key :
                self.table.pop(i)
                return
    
    def binary_search(self, key, low, high) :
        if (low <= high) :
            middle = (low + high) // 2
            if key == self.table[middle].key :
                return middle
            elif (key<self.table[middle].key) :
                return self.binary_search(key, low, middle - 1)
            else :
                return self.binary_search(key, middle + 1, high)
        return None

    def insert(self, key, value) :
        self.table.append(Entry(key, value))
        n = len(self.table)
        for i in range(1, n) :
            key = self.table[i]
            j = i-1
            while j>=0 and self.table[j].key > key.key :
                self.table[j + 1] = self.table[j]
                j -= 1
            self.table[j + 1] = key

    def size( self ):
        return len(self.table)
            

    def search(self, key) :
        pos = self.binary_search(key, 0, self.size()-1)
        if pos is not None : return self.table[pos]
        else : return None
