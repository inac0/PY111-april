"""
My little Stack
"""

stack = []

def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	stack.append(elem)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	try:
		return stack.pop()
	except IndexError:
		print("List is empty")

def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	try:
		return stack[-1 + ind]
	except IndexError:
		print("List is Empty")
	except AssertionError:
		print("List is out of range")


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	stack.clear()
	return None
