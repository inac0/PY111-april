"""
This module implements some functions based on linear search algo
"""

array = [10, 2, 4, 5, 7, 7, 8, 6, 22]

def min_search(arr) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	index1 = 0
	for i in range(1, len(arr)):
		if arr[index1] > arr[i]:
			index1 = i
	return index1

