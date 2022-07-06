def binary_search(ary, key, low, high) :
        if (low <= high) :
            middle = (low + high) // 2
            if key == ary[middle] :
                return middle
            elif (key<ary[middle]) :
                return binary_search(key, low, middle - 1)
            else :
                return binary_search(key, middle + 1, high)
        return None #탐색실패
