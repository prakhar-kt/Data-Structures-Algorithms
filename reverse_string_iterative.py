# Given a string, return the reversed string

def reverse_string_iterative(input):
    """
    :param input: string
    :return: reversed string
    """
    temp = ""

    for i in range(len(input)-1,0,-1):

        temp = temp + input[i]

    return temp

print(reverse_string_iterative("pirate's bay"))
print(reverse_string_iterative("Reverse this string"))



