def allPathsSourceTarget(self, graph):
	"""
	:type graph: List[List[int]]
	:rtype: List[List[int]]
	"""
	res = []
	end = len(graph) - 1
	def recurse(idx, path):
		if idx == end:
			res.append(path)
		for item in graph[idx]:
			recurse(item, path + [item])
	recurse(0, [0])
	return res

graph = [[1,2], [3], [3], []] 
print allPathsSourceTarget(graph)