from typing import Any
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def bfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""

	visited = []
	q = deque()
	q.append(start_node)
	while q:
		vertex = q.pop()
		if vertex not in visited:
			visited.append(vertex)
			print(g[vertex])
			q.extendleft(set(g[vertex]) - set(visited))
	return visited


if __name__ == "__main__":
	m = np.array([[0, 1, 0, 0, 1, 0],
			  [1, 0, 1, 0, 1, 0],
			  [0, 1, 0, 1, 0, 0],
			  [0, 0, 1, 0, 1, 1],
			  [1, 1, 0, 1, 0, 0],
			  [0, 1, 0, 1, 0, 0]])

	g = nx.Graph(m)
	nx.draw(g, with_labels = True)
	plt.show()
	print(bfs(g, 0))

