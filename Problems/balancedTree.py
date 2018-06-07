from binarytree import tree, bst, heap, build

# check root, if none return 0
# recurse left
# recurse right
# if abs of height(left-right) is over 1, return -1
# return 1 + max(left, right)

# return check root != -1

def is_balanced(root):

	def recurse(root):
		if root == None:
			return 0
		l = recurse(root.left)
		r = recurse(root.right)
		if abs(l-r) > 1:
			return -1
		return 1 + max(l,r)

	return recurse(root) != -1



my_tree = tree(height=3, is_perfect=False)
print(my_tree)
print is_balanced(my_tree)