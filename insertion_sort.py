# Sort an array using Insertion Sort

def insert_n_sort(array):
    """

    :param array: the array to be sorted array
    :return: sorted array
    """


    n = len(array)

    for i in range(1,n):

        for j in range(0,i):
            # Swap if any element before ith element is greater
            if array[j] > array[i]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

    return array

print(insert_n_sort([5,7,9,4,3,8,6]))
print(insert_n_sort([8,7,5,6,10,4,3]))
print(insert_n_sort([10,9,6,7,8,11]))






