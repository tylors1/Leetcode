
def averageOfLevels(root):
# set stack, first element is root
# while stack
#   reset level list, total, and count
#   while stack
#       node = stack.pop
#       if left node, append to level list
#       if right node, append to level list
#       add node value to total
#       add +1 to count
#   append to res, total / count
#   set stack = to level list        
       	if root == None:
            return []
        res = []
        stack = [root]
        
        while stack:
            level = []
            total = count = 0
            while stack:
                node = stack.pop()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                total += node.val
                count += 1
            res.append(float(total)/count)
            stack = list(level)
        return res
