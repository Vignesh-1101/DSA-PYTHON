class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Build a sample tree
root = TreeNode("Root")  # Root node
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")

root.children.append(child1)
root.children.append(child2)

# Adding children to Child 1
child1.children.append(TreeNode("Child 1.1"))
child1.children.append(TreeNode("Child 1.2"))

# Adding children to Child 2
child2.children.append(TreeNode("Child 2.1"))

# Print the tree
def print_tree(node, level=0):
    print(" " * (level * 2) + f"{node.value}")
    for child in node.children:
        print_tree(child, level + 1)

# print_tree(root)

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def level_order_traversal(root):
    if not root:
        return

    queue = deque([root])  # Initialize the queue with the root node

    while queue:
        current_node = queue.popleft() 
        print(current_node.value, end=" ")
        
        # Enqueue all children of the current node
        for child in current_node.children:
            queue.append(child)

# Example Tree
root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 3")

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

child1.children.append(TreeNode("Child 1.1"))
child1.children.append(TreeNode("Child 1.2"))

child2.children.append(TreeNode("Child 2.1"))

# Perform Level Order Traversal
print("Level Order Traversal:")
level_order_traversal(root)
