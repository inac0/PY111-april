def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	left_part = arr[0:(len(arr)//2)]
	print(left_part)
	right_part = arr[(len(arr)//2):-1]
	print(right_part)
	print(len(arr)//2)
	index = len(arr)//2
	if elem == arr[len(arr)//2]:
		return index
	elif elem > arr[len(arr)//2]:
		binary_search(elem, right_part)
	# 	index += len(arr)//2
	elif elem < arr[len(arr)//2]:
		binary_search(elem, left_part)
	return None