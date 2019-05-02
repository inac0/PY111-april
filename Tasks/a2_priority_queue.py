"""
Priority Queue

Queue priorities are from 0 to 5
"""

from heapq import heappush, heappop
import itertools

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of elements to entries
REMOVED = '<removed-elements>'      # placeholder for a removed
counter = itertools.count()     # unique sequence count

def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	if elem in entry_finder:
		remove_elem(elem)
	count = next(counter)
	entry = [priority, count, elem]
	entry_finder[elem] = entry
	heappush(pq, entry)
	return None

def remove_elem(elem):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(elem)
    entry[-1] = REMOVED

def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	while pq:
		priority, count, elem = heappop(pq)
		if elem is not REMOVED:
			del entry_finder[elem]
			return elem
		raise KeyError('pop from an empty priority queue')

def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	try:
		priority, count, elem = pq[ind]
		return elem
	except IndexError:
		print("Empty queue")


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	pq.clear()
	return None

