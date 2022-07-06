
def sort(ary) :
        n = len(ary)
        for i in range(1, n) :
            key = ary[i]
            j = i-1
            while j>=0 and ary[j] > key :
                ary[j + 1] = ary[j]
                j -= 1
            ary[j + 1] = key

ary = [5, 3, 8, 4, 9, 1, 6, 2, 7]
sort(ary)
print(ary)