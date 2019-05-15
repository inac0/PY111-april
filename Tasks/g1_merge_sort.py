from typing import List, TypeVar

_Tt = TypeVar("T")


def sort(container: List[_Tt]) -> List[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) > 1:
		mid = len(container) // 2
		left_part = container[:mid]
		right_part = container[mid:]

		sort(left_part)
		sort(right_part)

		i = j = k = 0

		while i < len(left_part) and j < len(right_part):
			if left_part[i] < right_part[j]:
				container[k] = left_part[i]
				i += 1
			else:
				container[k] = right_part[j]
				j += 1
			k += 1

		while i < len(left_part):
			container[k] = left_part[i]
			i += 1
			k += 1

		while j < len(right_part):
			container[k] = right_part[j]
			j += 1
			k += 1
	return container

