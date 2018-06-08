from binarytree import tree, bst, heap, build


# BFS
# if not root: return res
# init queue
# while items in queue:
# 	reset level, total, cnt
# 	while items in queue
# 		pop off queue
# 		append left then right to level
# 		add val to total, increment count
# 	append avg to res
# 	q = level


def avg(root):

	res=[]
	if not root: return res
	q=[root]
	while q:
		q1=[]
		total=0
		cnt=0
		while q:
			node =q.pop()
			if node.left: q1.append(node.left)
			if node.right: q1.append(node.right)
			total+=node.value
			cnt+=1
		res.append(total*1.0/cnt)
		q=list(q1)
	return res


my_tree = tree(height=3, is_perfect=False)
print(my_tree)
print avg(my_tree)