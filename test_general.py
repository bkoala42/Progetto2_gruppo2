from NewAVLTreeMap import NewAVLTreeMap
from TdP_collections.map.avl_tree import AVLTreeMap

"""
Remember per Ilaria:
    FB NEGATIVO A DESTRA
    FB POSITIVO A SINISTRA 
"""

t = NewAVLTreeMap()
print("\nInserting first element")
t[1] = "armando"
# print("tree is a leaf: ", t.is_leaf(t.root()))
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))


print("\nInserting second element")
t[5] = "aaa"
# print("tree is a leaf: ", t.is_leaf(t.root()))
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
print("5 balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))

#
#      1        FB = -1
#       \
#        5      FB = 0
#
# print("root is ", t.root().element()._key)
# print("right element is ", t.right(t.root()).element()._key)
# print("left element is ", t.left(t.root()))


print("\nInserting third element")
t[3] = "gg"
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
#
# #
# #     1    FB = -2              3     FB = 0
# #      \                      /   \
# #       5  FB = -1   ->      1     5  FB = 0
# #      /
# #     3    FB = 0
#
#
#
print("5 balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))
print("1 balance factor is: ", t.retrieve_balance_factor(t.left(t.root())))
# print("tree is balanced: ", t.is_balanced(t.root()))
# print("tree is a leaf: ", t.is_leaf(t.root()))
# print("left to the root there is: ", t.left(t.root()).element()._key)
# print("right to the root there is: ", t.right(t.root()).element()._key)
# print("Currently the tree has: ", t.num_children(t.root()), "children")


print("\nInserting fourth element")
t[10] = "bbb"

#
# #
# #      3      FB = -1
# #    /   \
# #   1     5   FB = -1
# #          \
# #           10    FB = 0
# #
#

print("tree is balanced: ", t.is_balanced(t.root()))
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
print("10 balance factor is: ", t.retrieve_balance_factor(t.right(t.right(t.root()))))
print("5 balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))
# print("right to the root there is: ", t.right(t.root()).element()._key)
# print("right to 5 there is: ", t.right(t.right(t.root())).element()._key)
# print("left to 5 there is: ", t.left(t.right(t.root())))

# print("Inserting fifth element")
# t[59] = "bb"
#
# for k,v in t.items():
#     print("[{}:{}]".format(k,v))
# print("root is: ", t.root().element()._key)
# print("root balance factor equals to: ", t.retrieve_balance_factor(t.root()))
# print("left to the root there is: ", t.left(t.root()).element()._key)
# print("right to the root there is: ", t.right(t.root()).element()._key)
# print("right to the right element there is: ", t.right(t.right(t.root())).element()._key)

#
# #
# #      3
# #    /   \
# #   1     10
# #        /  \
# #       5    59
# #
#
# print("height of the tree is ", t.height(p=t.left(t.root())))
#
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
