from collections import defaultdict
import heapq

def shortest_path(edges, start, end):

	graph = defaultdict(list)
	# adding nodes to graph, (cost, neighbor)
	for i, j, k in edges:
		graph[i].append((k, j))

	# init a queue
	queue = [(0, start, [])]
	visited = set()
	heapq.heapify(queue)

	while queue:
		(cost, node, path) = heapq.heappop(queue)
		if node not in visited:
			visited.add(node)
			path = path + [node]

			if node == end:
				return (cost, path)

			for c, neighbor in graph[node]:
				if neighbor not in visited:
					heapq.heappush(queue, (cost+c, neighbor, path))

	return -1


edges = [("A", "B", 7), ("A", "D", 5), ("D", "E", 3), ("B", "E", 2), ("D", "C", 3)]

print shortest_path(edges, "A", "C")