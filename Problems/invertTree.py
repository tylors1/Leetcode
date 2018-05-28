from binarytree import tree, bst, heap, build

def invert(root):
	head = root

	def recurse(root):
		if root:
			root.right, root.left = recurse(root.left), recurse(root.right)
			return root
	recurse(root)
	return head

my_tree = tree(height=3, is_perfect=False)
print(my_tree)
print invert(my_tree)