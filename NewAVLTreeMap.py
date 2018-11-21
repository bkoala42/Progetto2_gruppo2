from TdP_collections.map.avl_tree import AVLTreeMap
from TdP_collections.map.avl_tree import TreeMap


class NewAVLTreeMap(AVLTreeMap):
    # ---------------------------- override Position class ----------------------------
    class Position(AVLTreeMap.Position):
        def __init__(self, container, node):
            super().__init__(container, node)

        def get_node(self):
            """Returns the node stored at this Position."""
            return self._node

    class _Node(TreeMap._Node):
        """
        Node class for NewAVLTreeMap maintains balance factor value for balancing,
        calculated as the difference between the height of left subtree and the
        height of right subtree of the node in absolute value.
        """
        __slots__ = '_balance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0

        def get_balance_factor(self):
            return self._balance_factor

        def set_balance_factor(self, v):
            self._balance_factor = v

        def left_height(self):
            pass
            # return self._left._height if self._left is not None else 0

        def right_height(self):
            pass
            # return self._right._height if self._right is not None else 0

    # TODO should this method be static?
    def retrieve_balance_factor(self, p):
        """
        Utility method to get balance factor inside the node from position
        without accessing the protected members _node and _balance_factor.
        This is achieved by adding respectively:
            a get_node() method to the Position(LinkedBinaryTree.Position) class and
            a get_balance_factor() method to the _Node(TreeMap._Node) class.
        :param p: position
        :return: balance factor associated to the node inside the position
        """
        return p.get_node().get_balance_factor()

    # TODO should this method be static?
    def change_balance_factor(self, p, v):
        """
        Utility method to set balance factor into the node from position without
        accessing the protected members _node and _balance_factor.
        This is achieved by adding respectively:
            a get_node() method to the Position(LinkedBinaryTree.Position) class and
            a set_balance_factor() method to the _Node(TreeMap._Node) class.
        :param p: position
        :param v: value of the balance factor to set
        """
        p.get_node().set_balance_factor(v)

    def _compute_height(self, p):
        return self.height(p)

    def _recompute_balance_factor(self, p):
        #if self.left(p) is not None and self.right(p) is not None:                                         # base case root position without children
        #                                                                 # nothing must be done since balance factor
        #                                                                 # is already 0.
        #     bf = self.retrieve_balance_factor(p)                        # save current balance factor in :var bf
        #     # if self.left(p) is None and self.right(p) is not None:      # base case insert to the right
        #     #     # p._node._balance_factor = p._node._balance_factor - 1
        #     #     self.change_balance_factor(p, bf - 1)
        #     #     return
        #     # elif self.right(p) is None and self.left(p) is not None:    # base case insert to the left
        #     #     # p._node._balance_factor = p._node._balance_factor + 1
        #     #     self.change_balance_factor(p, bf + 1)
        #     #     return
        #     # elif self.retrieve_balance_factor(self.left(p)) == 0 \
        #     #         and self.retrieve_balance_factor(self.right(p)) != 0:
        #     #     self.change_balance_factor(p, bf - 1)
        #     #     return
        #     # elif self.retrieve_balance_factor(self.right(p)) == 0 \
        #     #         and self.retrieve_balance_factor(self.left(p)) != 0:
        #     #     self.change_balance_factor(p, bf + 1)
        #     #     return
        #     # elif self.retrieve_balance_factor(self.right(p)) == 0 \
        #     #         and self.retrieve_balance_factor(self.left(p)) == 0:
        #     #     self.change_balance_factor(p, bf)
        #     #     return
        #     # elif self.left(p)._node._balance_factor == 0:               # trinode cases
        #     #      p._node._balance_factor = 0
        #
        if self.left(p) is None and self.right(p) is None:
            self.change_balance_factor(p, 0)
            return
        if self.left(p) is None:
            self.change_balance_factor(p, -1)
            return
        elif self.right(p) is None:
            self.change_balance_factor(p, 1)
            return
        if self.retrieve_balance_factor(self.left(p)) == 0:
            self.change_balance_factor(p, 0)
            return
        # elif self.left(p)._node._balance_factor == -1:
        #     p._node._balance_factor = 1
        elif self.retrieve_balance_factor(self.left(p)) == -1:
            self.change_balance_factor(p, 1)
            return
        # elif self.left(p)._node._balance_factor == 1:
        #     p._node._balance_factor = -1
        elif self.retrieve_balance_factor(self.left(p)) == 1:
            self.change_balance_factor(p, -1)
            return
        # elif self.right(p)._node._balance_factor == 0:
        #     p._node._balance_factor = 0
        elif self.retrieve_balance_factor(self.right(p)) == 0:
            self.change_balance_factor(p, 0)
            return
        # elif self.right(p)._node._balance_factor == -1:
        #     p._node._balance_factor = 1
        elif self.retrieve_balance_factor(self.right(p)) == -1:
            self.change_balance_factor(p, 1)
            return
        # elif self.left(p)._node._balance_factor == 1:
        #     p._node._balance_factor = -1
        elif self.retrieve_balance_factor(self.right(p)) == 1:
            self.change_balance_factor(p, -1)
            return


        # se p è il figlio sinistro

        """
        if self.left(self.parent(p)) == p:
            self.change_balance_factor(p, -max(self.retrieve_balance_factor(self.parent(p)), 0))
        # se p è il figlio destro
        elif self.right(self.parent(p)) == p:
            self.change_balance_factor(p, -min(self.retrieve_balance_factor(self.parent(p)), 0))
        else:
            self.change_balance_factor(p, 0)
        """
    def _update_rebalance_factor(self, p, insert=True):
        if insert:
            if p == self.left(self.parent(p)):
                self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) + 1)
                return
            else:
                self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) - 1)
                return
        else:
            if self.right(p) is None and self.left(p) is None:
                 # salgo da destra
                if self.right(self.parent(p)) == p:
                    self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) + 1)
                # salgo da sx
                else:
                    self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) - 1)
                self.change_balance_factor(p, 0)
                return
            elif self.left(p) is None:
                self.change_balance_factor(p, self.retrieve_balance_factor(p) - 1)
            elif self.right(p) is None:
                self.change_balance_factor(p, self.retrieve_balance_factor(p) + 1)

        # if p == self.left(self.parent(p)):
        #     if insert:
        #         self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) + 1)
        #     else:
        #         if self.left(p) is None:
        #             self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) - 1)
        #         elif self.right(p) is None:
        #             self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) + 1)
        # elif p == self.right(self.parent(p)):
        #     if insert:
        #         self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) - 1)
        #     else:
        #         if self.left(p) is None:
        #             self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) - 1)
        #         elif self.right(p) is None:
        #             self.change_balance_factor(self.parent(p), self.retrieve_balance_factor(self.parent(p)) + 1)
        # else:
        #     raise Exception("Position not recognized")

    def _isbalanced(self, p):
        return abs(self.retrieve_balance_factor(p)) <= 1

    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
        _ = self._validate(p)
        # esiste il caso -2/+2???
        # if p._node._balance_factor == 0 and favorleft:
        if self.retrieve_balance_factor(p) == 0 and favorleft:
            return self.left(p)
        # elif p._node._balance_factor > 0:
        elif self.retrieve_balance_factor(p) > 0:
            return self.left(p)
        # elif p._node._balance_factor < 0:
        elif self.retrieve_balance_factor(p) < 0:
            return self.right(p)

    def _rebalance(self, p, insert):
        # while p is not None:
        #     old_balance_factor = self.retrieve_balance_factor(p)
        #     if not self._isbalanced(p):
        #         p = self._restructure(self._tall_grandchild(p))
        #         self._recompute_balance_factor(self.left(p))
        #         self._recompute_balance_factor(self.right(p))
        #         self._recompute_balance_factor(p)
        #         if self.retrieve_balance_factor(p) == old_balance_factor:
        #             p = None  #
        #     else:
        #         p = self.parent(p)

        while p is not None:
            if self.parent(p) is not None:
                old_father_bf = self.retrieve_balance_factor(self.parent(p))
                self._update_rebalance_factor(p, insert)                       # +,-1 con insert e delete
                old_balance_factor = self.retrieve_balance_factor(p)
                if not self._isbalanced(self.parent(p)):
                    # print(p.element()._key)
                    if self.parent(self.parent(p)) is None:
                        # print(self._tall_child(p).element()._key)
                        p = self._restructure(self._tall_child(p))
                    else:
                        # print(self._tall_grandchild(p).element()._key)
                        p = self._restructure(self._tall_grandchild(self.parent(p)))
                    self._recompute_balance_factor(self.left(p))
                    self._recompute_balance_factor(self.right(p))
                    self._recompute_balance_factor(p)
                if insert and (old_father_bf == 1 or old_father_bf == -1) and self.retrieve_balance_factor(p) == 0:
                    return
                if insert and self.retrieve_balance_factor(p) == 0 and (old_balance_factor == 1 or old_balance_factor == -1):
                    return
                if not insert and (self.retrieve_balance_factor(p) == 1 or self.retrieve_balance_factor(p) == -1) and old_balance_factor == 0:
                    return
            # Caso delete di un sotto albero della root
            elif not insert:
                self._update_rebalance_factor(p, insert=False)
                p = self._restructure(self._tall_grandchild(p))
                if self.left(p) is not None:
                    self._recompute_balance_factor(self.left(p))
                if self.right(p) is not None:
                    self._recompute_balance_factor(self.right(p))
                self._recompute_balance_factor(p)
                return
            p = self.parent(p)

            # if self.parent(p) is not None and self.is_balanced(p):
            #     self._recompute_balance_factor(self.parent(p))
            # # old_balance_factor = self.retrieve_balance_factor(p)
            # if not self.is_balanced(p):
            #     if not self.is_root(p):
            #         old_balance_factor = self.retrieve_balance_factor(self.parent(p))
            #     else:
            #         old_balance_factor = self.retrieve_balance_factor(p)
            #     # Enters if -2/+2 is detected
            #     p = self._restructure(self._tall_grandchild(p))
            #     # print(p.element()._key)
            #     # print(self.left(p).element()._key)
            #     # print(self.right(p).element()._key)
            #     self._recompute_balance_factor(self.left(p))
            #     self._recompute_balance_factor(self.right(p))
            #     #
            #     self._recompute_balance_factor(p)
            #     #
            #     # self._recompute_balance_factor(self.parent(p))
            #     if self.retrieve_balance_factor(p) == old_balance_factor:  # has height changed?
            #         p = None  # no further changes needed
            # else:
            #     p = self.parent(p)

    # ----------- method for test purpose

    def is_balanced(self, p):
        return self._isbalanced(p)

    def _rebalance_insert(self, p):
        self._rebalance(p, True)

    def _rebalance_delete(self, p):
        self._rebalance(p, False)

    # def _rotate(self, p):
    #     """Rotate Position p above its parent."""
    #     x = p._node
    #     y = x._parent  # we assume this exists
    #     z = y._parent  # grandparent (possibly None)
    #     if z is None:
    #         self._root = x  # x becomes root
    #         x._parent = None
    #     else:
    #         self._relink(z, x, y == z._left)  # x becomes a direct child of z
    #     # now rotate x and y, including transfer of middle subtree
    #     if x == y._left:
    #         self.change_balance_factor(y, self.retrieve_balance_factor(y) - 1)
    #         self.change_balance_factor(x, -self.retrieve_balance_factor(y))
    #         self._relink(y, x._right, True)  # x._right becomes left child of y
    #         self._relink(x, y, False)  # y becomes right child of x
    #     else:
    #         self.change_balance_factor(y, self.retrieve_balance_factor(y) + 1)
    #         self.change_balance_factor(x, -self.retrieve_balance_factor(y))
    #         self._relink(y, x._left, False)  # x._left becomes right child of y
    #         self._relink(x, y, True)  # y becomes left child of x
