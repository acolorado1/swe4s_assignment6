import sys


# perform linear search where L is a list a k is a value in that list
def linear_search(L, k):
    current_value = -1

    # make sure that variable is a list
    if isinstance(L, list):
        pass
    else:
        raise TypeError("Variable is not of list type")

    # for every index in the list
    for index in range(len(L)):
        current_value = L[index]
        # find index of key
        if k == current_value:
            return index
        else:
            current_value = -1

    # if no index is found
    if current_value == -1:
        print('no index found')
        sys.exit(1)


# take a list and create list of tuples containing list value and index
def index_list(L):
    index_list = []

    if len(L) != 0:
        pass
    else:
        raise ValueError("This is an empty list")

    # for each item in list
    for index in range(len(L)):
        index_list.append((L[index], index))

    # sort by the value in the original list
    index_list.sort(key=lambda tup: tup[0])
    return index_list


# perform a binary search on a list
def binary_search(L, k):

    # make sure that variable is a list
    if isinstance(L, list):
        pass
    else:
        raise TypeError("Variable is not of list type")

    high = len(L)
    low = -1

    # until high and low values have reversed
    while high - low > 1:
        mid = (high + low) // 2

        # if first index in tuple matches the key
        if k == L[mid][0]:
            return L[mid][1]

        # if key is less than the first index of the tuple
        if k.lower() < L[mid][0].lower():
            high = mid
        else:
            low = mid

    return -1
