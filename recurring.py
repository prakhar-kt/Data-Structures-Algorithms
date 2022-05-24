# Problem Statement :
# Given an array, return the first recurring character

def first_recurring(array):
    """
    :param array: a list
    :return: the first recurring character, or None if no recurring character

    """
    dict = {}
    for i in range(len(array)):

        if array[i] in dict:
            return array[i]
        else:
            dict[array[i]] = 1



    return None

print(first_recurring([2,1,3,5,8,1,2]))
# assert first_recurring([2,1,3,5,8,3,2]) == 2
print(first_recurring([]))

print(first_recurring([1,2,3,5,8]))






