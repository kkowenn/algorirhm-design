class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root: return None
        q = [root]
        while q:
            rightNode = None
            size = len(q)
            for _ in range(size):
                cur = q.pop(0)
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return root

def print_tree_next_connections(root):
    # Function to print tree nodes' next connections (level by level)
    levels = []
    q = [(root, 0)]
    while q:
        node, level = q.pop(0)
        if node:
            if len(levels) <= level:
                levels.append([])
            levels[level].append(node.val if node.next is None else f"{node.val}->{node.next.val}")
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
    return levels

# Constructing a simple binary tree
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sol = Solution()
sol.connect(root)

# Print the tree's next connections
print_tree_next_connections(root)
