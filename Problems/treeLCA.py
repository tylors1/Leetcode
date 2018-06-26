from binarytree import Node

def LCA(root, n1, n2):
	print root
	arr1 = []
	arr2 = []

	def getPath(root, path, n):
		if not root:
			return False

		path.append(root.value)
		if root.value == n:
			return True
		if (root.left != None and getPath(root.left, path, n)) or (root.right != None and getPath(root.right, path, n)):
			return True

		path.pop()
		return False

	getPath(root, arr1, n1)
	getPath(root, arr2, n2)

	i = 0
	while i < len(arr1) and i < len(arr2):
		if arr1[i] != arr2[i]:
			break
		i += 1
	return arr1[i-1]





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print LCA(root, 4, 5)