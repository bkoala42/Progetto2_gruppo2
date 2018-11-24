from pkg_1.NewAVLTreeMap import NewAVLTreeMap

"""
Remember per Ilaria:
    FB NEGATIVO A DESTRA
    FB POSITIVO A SINISTRA 
"""

t = NewAVLTreeMap()
print("\nInserting first element")
t[1] = "armando"
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
print("root is: ", t.root().element()._key)
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

# print("tree is balanced: ", t.is_balanced(t.root()))
print("root is: ", t.root().element()._key)
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
print("10 balance factor is: ", t.retrieve_balance_factor(t.right(t.right(t.root()))))
print("5 balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))
print("1 balance factor is: ", t.retrieve_balance_factor(t.left(t.root())))
# print("right to the root there is: ", t.right(t.root()).element()._key)
# print("right to 5 there is: ", t.right(t.right(t.root())).element()._key)
# print("left to 5 there is: ", t.left(t.right(t.root())))

print("\nInserting fifth element")
t[59] = "bb"
#
#
# #
# #      3                  FB = -1
# #    /   \
# #   1     10              FB = 0, FB = 0
# #        /  \
# #       5    59           FB = 0, FB = 0
# #
#
#
# for k,v in t.items():
#     print("[{}:{}]".format(k,v))
print("root is: ", t.root().element()._key)
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
print("10 balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))
print("59 balance factor is: ", t.retrieve_balance_factor(t.right(t.right(t.root()))))
print("5 balance factor is: ", t.retrieve_balance_factor(t.left(t.right(t.root()))))
print("1 balance factor is: ", t.retrieve_balance_factor(t.left(t.root())))
# print("left to the root there is: ", t.left(t.root()).element()._key)
# print("right to the root there is: ", t.right(t.root()).element()._key)
# print("right to the right element there is: ", t.right(t.right(t.root())).element()._key)

#
# TODO SKIP THIS CASE
# print("\nDeleting root element")
# t.delete(t.root())
# #
# # #
# # #      10
# # #    /   \
# # #   1     59
# # #    \
# # #     5
# #
# print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
# print("59 balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))
# print("1 balance factor is: ", t.retrieve_balance_factor(t.left(t.root())))
# print("5 balance factor is: ", t.retrieve_balance_factor(t.right(t.left(t.root()))))

# TODO TRY THIS
# Quello che ci manca è il caso in cui si muove la radice,
# non possiamo solo mettere a zero perchè la radice può essere anche
# cancellata oppure spostata in seguito a rebalance
print("\nInserting sixth element")
t[42] = "bb"
#
# #
# #       10
# #     /    \
# #    3      59
# #   / \    /
# #  1   5  42
# #
#
#
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
print("root is: ", t.root().element()._key)
print("59 balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))
print("3 balance factor is: ", t.retrieve_balance_factor(t.left(t.root())))

print("\nInserting seventh element")
t[17] = "bb"
#
# #
# #       10
# #     /    \
# #    3      42
# #   / \    /  \
# #  1   5  17   59
# #
#
#
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
print("root is: ", t.root().element()._key)
print("42 balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))
print("3 balance factor is: ", t.retrieve_balance_factor(t.left(t.root())))
#
#
del t[59]  # 59
del t[17]
# #
# # #
# # #         10        FB = 0
# # #       /    \
# # #      3     42    FB = 1
# # #     / \    / \
# # #           17  59
# # #
# #
#
print("\nDeleting 59")
print("tree balance factor is: ", t.retrieve_balance_factor(t.root()))
print("right balance factor is: ", t.retrieve_balance_factor(t.right(t.root())))
print("left balance factor is: ", t.retrieve_balance_factor(t.left(t.root())))
