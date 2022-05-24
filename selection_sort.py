# Sort an array using selection sort

def select_sort(array):
    """
    :param array: the array to be sorted
    :return: the sorted array with elements arranged in ascending order
    """
    n = len(array)
    for i in range(n-1):
        for j in range(i+1,n):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array

print(select_sort([6,3,8,5,4,7,10,9]))
print(select_sort([2,3,11,8,5,1,7,8,9,]))


