from typing import Any
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt



def dfs(g: nx.Graph, start_node: Any) -> list:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	visited = []
	stack = [start_node]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.append(vertex)
			stack.extend(set(g[vertex]) - set(visited))
	return ''.join(visited)

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
	print(dfs(g, 0))
