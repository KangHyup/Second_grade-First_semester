#버블정렬

ary = [7, 4, 9, 6, 3, 8, 7, 5]

def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        bChanged = False
        for j in range(i):
            if(A[j]>A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
    
        if not bChanged: break;
        print(A)

bubble_sort(ary)

def interpolation_search(A, key, low, high):
    if(low <= high):
        middle = int(low+(high-low)*(key-A[low]) / (A[high] - A[low]))
        print(A[middle])
        if key == A[middle]:
            return middle
        elif(key < A[middle]):
            return interpolation_search(A, key, low, middle-1);
        else:
            return interpolation_search(A, key, middle+1, high)
    return None

ary = [ 8, 11, 12, 15, 16, 19, 20, 23, 25, 28, 29, 31, 33, 35, 38, 40]
interpolation_search(ary, 28, 0, 15)




