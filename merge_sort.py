# Sort an array using divide and conquer

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        L = merge_sort(L)
        R = merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i + 1
            else:
                arr[k] = R[j]
                j = j+1
            k = k+1

        while i < len(L):
            arr[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            arr[k] = R[j]
            j = j + 1
            k = k + 1

    return arr



print(merge_sort([6,4,3,7,10,8,9,4,2,1]))
print(merge_sort([7,1,6,4,9,3,2,10,12]))











