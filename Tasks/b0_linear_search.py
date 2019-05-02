"""
This module implements some functions based on linear search algo
"""


def min_search(arr) -> int:
    """
    Function that find minimal element in array.

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    index1 = 0
    for i in range(1, len(arr)):
        if arr[index1] > arr[i]:
            index1 = i
    return index1
