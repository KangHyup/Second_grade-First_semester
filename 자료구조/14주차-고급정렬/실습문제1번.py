
def heapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+1

    if l<n and arr[i] < arr[l]: largest=l
    if r<n and arr[largest] < arr[i]: largest=r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    print("i=", 0, arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
        print("i=", i, arr)
    print()

    for i in range(n-1, 0, -1):
        heapify(arr, i, 0)
        print("i=", i, arr)

    return arr
ary = [5, 3, 8, 4, 9, 1, 6, 2, 7]
ary = heapSort(ary)
print("HeapSort: ", ary)
