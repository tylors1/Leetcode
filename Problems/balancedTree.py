from binarytree import tree, bst, heap, build

def is_balanced(root):

	def recurse(root):
		if root == None:
			return 0

		l = recurse(root.left)
		r = recurse(root.right)
		print l, r
		if abs(l-r) > 1 or l == -1 or r == -1:
			return -1
		return max(l, r)
	return recurse(root) != -1


my_tree = tree(height=3, is_perfect=False)
print(my_tree)
print is_balanced(my_tree)