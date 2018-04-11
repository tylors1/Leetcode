# PROMPT: 
# 
# You're given a list of words which are lexicographically (i.e. alphabetically) sorted. 
# Write a function which prints the lexicographic order of the characters. 
# Note: won't be the same as the Roman alphabet.

# input: 
# words = [
# "one",
# "son",
# "soon",
# "eon"]


# output: ["n", "o", "s", "e"]


# GRAPH 


class Graph:
    def __init__(self):
        # {{{
        self.storage = {}
  
  
    # Time Complexity: O(1)
    # Auxiliary Space Complexity: O(1)
    def add_vertex(self, id):
        # {{{
        if id not in self.storage:
            self.storage[id] = []
            return True
        else:
            return False

    # Time Complexity: O(V+E)
    # Auxiliary Space Complexity: O(1)
    def remove_vertex(self, id):
        # {{{
        if id not in self.storage:
            return False

        for vertex in self.storage:
            edges = self.storage[vertex]
            if id in edges:
                edges.remove(id)

        del self.storage[id]
        return True

    # Time Complexity: O(1)
    # Auxiliary Space Complexity: O(1)

    def add_edge(self, id1, id2):
        # {{{
        if id1 not in self.storage or id2 not in self.storage:
            return False
        if id2 in self.storage[id1]:
            return False
        self.storage[id1].append(id2)
        return True

    # Time Complexity: O(E)
    # Auxiliary Space Complexity: O(1)

    def remove_edge(self, id1, id2):
        # {{{
        if id1 in self.storage:
            if id2 in self.storage[id1]:
                self.storage[id1].remove(id2)
                return True
        return False
      
      
    # Time Complexity: O(1)
    # Auxiliary Space Complexity: O(1)

    def is_vertex(self, id):
        # {{{
        return id in self.storage

    # Time Complexity: O(1)
    # Auxiliary Space Complexity: O(1)

    def neighbors(self, id):
        if id in self.storage:
            return self.storage[id]
        return None


def topological_sort(graph):
  visited = set()
  result = []

  def dfs(current):
    if current in visited:
      return

    visited.add(current)
    neighbors = graph.storage[current]
    for neighbor in neighbors:
      dfs(neighbor)
    result.append(current)

  for node in graph.storage.keys():
    dfs(node)

  return list(reversed(result))

    
def lexicographic_order(words):
  graph = Graph()
  for i in range(len(words))[:-1]:
    for j in range(len(words[i])):
      if j >= len(words[i]) or j >= len(words[i+1]):
        break
      if words[i][j] != words[i+1][j]:
        graph.add_vertex(words[i][j])
        graph.add_vertex(words[i+1][j])
        graph.add_edge(words[i][j], words[i+1][j])
        break
  return topological_sort(graph)

  


print(lexicographic_order(["one", "son", "soon", "eon"])) # ["n", "o", "s", "e"]
print(lexicographic_order(["toll","loo","lot"]))
    


# s --> e --> n --> o 







