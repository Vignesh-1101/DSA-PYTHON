class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, children):
        self.children.append(children)

tree = TreeNode("Drinks",children=[])
hot = TreeNode("Hot",children=[])
cold = TreeNode("Cold",children=[])
tree.add_child(hot)
tree.add_child(cold)
tea = TreeNode("Tea",children=[])
coffee = TreeNode("Coffee",children=[])
cola = TreeNode("Cola",children=[])
fanta = TreeNode("Fanta",children=[])
hot.add_child(tea)
hot.add_child(coffee)
cold.add_child(cola)
cold.add_child(fanta)
print(tree)