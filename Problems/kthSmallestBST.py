from binarytree import tree, bst, heap

my_bst = bst(height=3, is_perfect=False)
k = 5

def find_smallest(my_bst, k):
	count = 0
	stack = []
	root = my_bst
	while True:
		while root:
			stack.append(root)
			root = root.left

		root = stack.pop()
		count += 1
		if count == k:
			return root.value
		root = root.right






print my_bst
print find_smallest(my_bst, k)