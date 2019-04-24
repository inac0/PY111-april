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



def min_weight_search(Graph) -> tuple:
	"""
	Function that find edge in graph with minimal weight of all

	:param Graph: NetworkX Graph (or digraph) with weighted edges
	:return: tuple of nodes (node, node) the weight of edge between which is minimal (any occurrence)
	"""
	return None, None


print(min_search(array))