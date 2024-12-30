#atmost 2 children
"""
full binary tree:
perfect binary tree: 
complete binary tree: 
balanced binary tree: same distance from root node
"""

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
        pass

newBT = TreeNode("Drinks") #O(1)
left = TreeNode("Hot")
right = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("coffee")
fanta = TreeNode("Fanta")
cola = TreeNode("Cola")
newBT.left = left
newBT.right = right
left.left = tea
left.right = coffee
right.left = cola
right.right = fanta

def preorder(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preorder(rootNode.left)
    preorder(rootNode.right)

preorder(newBT)
print("postOrder------------")

def postorder(rootNode):
    if not rootNode:
        return
    postorder(rootNode.left)
    postorder(rootNode.right)
    print(rootNode.value)

postorder(newBT)

print("inOrder------------")
def inorder(rootNode):
    if not rootNode:
        return
    inorder(rootNode.left)
    print(rootNode.value)
    inorder(rootNode.right)

inorder(newBT)

print("leveorder-----------------")

def levelOrder(rootNode):
    if not rootNode:
        return
    queue = [rootNode]
    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

levelOrder(newBT)

from collections import deque
def right_view(root):
    if not root:
        return []

    queue = deque([root])  # Queue for level order traversal
    right_side = []

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # If this is the last node in the current level, add it to the right view
            if i == level_size - 1:
                right_side.append(node.value)
            # Add left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_side

print(right_view(newBT))

from collections import deque, OrderedDict

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def top_view(root):
    if not root:
        return []

    # Queue for level-order traversal (stores pairs of node and its horizontal distance)
    queue = deque([(root, 0)])
    # Dictionary to store the first node at each horizontal distance
    hd_map = {}

    while queue:
        node, hd = queue.popleft()

        # If the horizontal distance is not in the map, add the node
        if hd not in hd_map:
            hd_map[hd] = node.value

        # Add the left and right children with updated horizontal distances
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Sort the map by horizontal distance and return the values
    return [hd_map[key] for key in sorted(hd_map.keys())]
print(top_view(newBT))


def searchBT(node, levelOrder):
    if not node:
        return
    if levelOrder == node.value:
        return "True"
    return searchBT(node.left, levelOrder) or searchBT(node.right, levelOrder)

print(searchBT(newBT, "Tea"))

# class BinaryTree(TreeNode):
#     pass