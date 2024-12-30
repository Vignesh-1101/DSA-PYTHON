class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive function to process nodes at the current level
def print_level(node, level):
    if not node:
        return False  # Indicates no nodes were printed at this level
    
    if level == 1:  # Print the node value if we reach the target level
        print(node.value, end=" ")
        return True  # Node was processed successfully
    
    # Recursively process left and right subtrees for the next level
    left = print_level(node.left, level - 1)
    right = print_level(node.right, level - 1)
    
    return left or right  # Return True if any nodes were printed at this level

# Function to perform Level Order Traversal using recursion and while loop
def level_order_traversal_recursive(root):
    level = 1  # Start with level 1
    while print_level(root, level):  # Continue processing levels until no nodes are left
        level += 1  # Move to the next level

# Example Binary Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform Level Order Traversal
print("Level Order Traversal (Recursive with While Loop):")
level_order_traversal_recursive(root)

max_diameter = 0
def diameter(node):
    if not node: 
        return 0
            
    left_height = diameter(node.left)
    right_height = diameter(node.right)
            
    max_diameter = max(max_diameter, left_height + right_height)
    return 1 + max(left_height, right_height)