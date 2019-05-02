"""
My little Queue
"""

queue = []

def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	queue.append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	try:
		return queue.pop(0)
	except IndexError:
		print("Empty queue")


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	try:
		return queue[ind]
	except IndexError:
		print("Empty queue")


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	queue.clear()
	return None
