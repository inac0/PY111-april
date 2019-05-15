from typing import List, TypeVar
import random

_Tt = TypeVar("T")


def sort(container: List[_Tt]) -> List[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	if len(container) <= 1:
		return container
	else:
		pivot_num = random.choice(container)
		equal_num = []
		small_num = []
		big_num = []
		for i in container:
			if i < pivot_num:
				small_num.append(i)
			elif i > pivot_num:
				big_num.append(i)
			else:
				equal_num.append(i)
		container = sort(small_num) + equal_num + sort(big_num)
		return container

# def sort2(container: List[_Tt]) -> List[_Tt]:
# 	"""
# 	Sort input container with quick sort
#
# 	:param container: container of elements to be sorted
# 	:return: container sorted in ascending order
# 	"""
#
# 	if len(container) <= 1:
# 		return container
# 	else:
# 		pivot_num = random.choice(container)
# 		left_counter = 0
# 		right_counter = 0
# 		for i, j in enumerate(container):
# 			if j < pivot_num:
# 				container[i], container[left_counter] = container[left_counter], container[i]
# 				left_counter += 1
# 				container[i], container[right_counter] = container[right_counter], container[i]
# 				right_counter += 1
# 			elif j == pivot_num:
# 				container[i], container[right_counter] = container[right_counter], container[i]
# 				right_counter += 1
# 			elif j > pivot_num: continue
# 		container = sort(container[:left_counter]) + container[left_counter:right_counter] + sort(container[right_counter:])
# 		return container


