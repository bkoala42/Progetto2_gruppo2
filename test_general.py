from NewAVLTreeMap import NewAVLTreeMap
from TdP_collections.map.avl_tree import AVLTreeMap

t = NewAVLTreeMap()
print("Inserting first element")
t[1] = "armando"
print("Inserting second element")
t[5] = "aaa"

#
#      1
#       \
#        5
#
print("root is ", t.root().element()._key)
print("right element is ", t.right(t.root()).element()._key)
print("left element is ", t.height(p=None))
# print(t.first()._node.get_rebalance_factor())

print("Inserting third element")
t[3] = "gg"
#
# #
# #      3
# #    /   \
# #   1     5
# #
#
# # print(t.after(t.first()))
#
#
# # print(t.is_balanced(t.first()))
# # print(t.is_leaf(t.first()))
# # print(t.num_children(t.first()))
print("Inserting fourth element")
t[10] = "bbb"
print("height of the tree is ", t.height(p=None))

#
# #
# #      3
# #    /   \
# #   1     5
# #          \
# #           10
# #
#

print("Inserting fifth element")
t[59] = "bb"

#
# #
# #      3
# #    /   \
# #   1     10
# #        /  \
# #       5    59
# #
#
print("height of the tree is ", t.height(p=t.left(t.root())))

# t[2] = "bb"
# t.delete(t.find_position(2))
#
# #
# #      3
# #    /   \
# #   1     10
# #        /  \
# #       5    59
# #
#
#
# for k,v in t.items():
#     print("[{}:{}]".format(k,v))
#
# t[4] = "bb"
# t[6] = "bb"
#
# #
# #      3
# #    /   \
# #   1     5
# #
#
