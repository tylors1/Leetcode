from binarytree import tree, bst, heap, build


my_tree = tree(height=3, is_perfect=False)

print(my_tree)


def de_serialize(root)

	stack = [root]
	res = []
	while stack:
		node = stack.pop()
		if node:
			res.append(node.value)
			stack.append(node.right)
			stack.append(node.left)
		else:
			res.append(-1)

	return ' '.join(str(item) for item in res)

def serialize(nodes):
	print nodes.split(" ")



nodes = de_serialize(my_tree)

print serialize(nodes)





"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        
        stack = [root]
        visited = {}
        res = []

        while stack:
            node = stack[-1]
            
            if not node.children or node in visited:
                res.append(stack.pop().val)
            else:
                for child in node.children[::-1]:
                    stack.append(child)
                visited[node] = True
        return res
    
    
    
    
    
    