def merge_sorted_arrays(arr1, arr2):
    '''

    :param arr1: a sorted array
    :param arr2: a sorted array
    :return: array obtained after merging arr1 and arr2
    '''

    # if the length of either array is zero, return the other array
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    # define a merged array with None values and the length the same as the 2 other arrays
    merged_array = [None] * (len(arr1) + len(arr2))

    i=0
    j=0
    k=0

    # while i and j are less than length of arr1 and arr2
    while (i < len(arr1)) & (j < len(arr2)):
        if arr1[i] < arr2[j]:
            merged_array[k] = arr1[i]
            i = i+1
            k = k+1
        else:
            merged_array[k] = arr2[j]
            j = j+1
            k = k+1

    # In case of len(arr1) != len(arr2)
    # one of the arrays will have some elements left, which we
    # will push to the end of the merged arrays

    while i < len(arr1):
        merged_array[k] = arr1[i]
        i = i+1
        k = k+1

    while j < len(arr2):
        merged_array[k] = arr2[j]
        j = j+1
        k = k+1

    return merged_array



print(merge_sorted_arrays([0,2,4,7,10], [3,6,8,10,12]))





