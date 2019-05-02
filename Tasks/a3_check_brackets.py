def check_brackets(brackets_row: str) -> bool:
    """
	Check whether input string is a valid bracket sequence
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
    mapping = dict(zip('({[', ')}]'))
    queue = []
    for letter in brackets_row:
        if letter in mapping:
            queue.append(mapping[letter])
        elif letter not in mapping.values():
            raise ValueError('Unknown letter {letter}'.format(letter=letter))
        elif not (queue and letter == queue.pop()):
            return False
    return not queue
