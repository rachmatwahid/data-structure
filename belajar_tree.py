# ====
# TREE
# ====

from anytree import Node, RenderTree

root = Node("Budi")

first_level_child1 = Node("Nina", parent=root)
first_level_child2 = Node("Ari", parent=root)

second_level_child1 = Node("Lia", parent=first_level_child1)
second_level_child2 = Node("Wawan", parent=first_level_child1)
second_level_child3 = Node("Dina", parent=first_level_child2)

# for pre, fill, node in RenderTree(root):
#     print("%s%s" % (pre, node.name))

print(RenderTree(root))
