# Sort an array in ascending order

def bubble_sort(array):
    """

    :param array: an array to be sorted
    :return: a sorted array from lowest to highest
    """

    # Define a boolean marker for the while loop
    marker = True

    # Run the while loop as long as there are elements not in ascending order
    while marker == True:
        # Initialise a count that keeps track of the number of exchanges
        count = 0
        # iterate over the items of the array
        for i in range(0,len(array)-1):
            # sort by taking 2 elements at a time
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                count = count + 1 # increase the count if sorting has taken place

        # if no sorting takes place even after one loop over the array, the count will remain 0
        # and we can stop the iteration
        if count == 0:
            marker = False

    return array


print(bubble_sort([6,3,5,8,9,7,4]))
print(bubble_sort([]))
print(bubble_sort([3,0,2,10,9,20,14]))
