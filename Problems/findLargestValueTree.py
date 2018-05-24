from binarytree import tree, bst, heap, build

def find_largest(root):
	if root == None:
		return float('-inf')
	res = root.value
	lres = find_largest(root.left)
	rres = find_largest(root.right)
	res = max(lres, res, rres)

	return res



	


my_tree = tree(height=3, is_perfect=False)
print(my_tree)
print find_largest(my_tree)