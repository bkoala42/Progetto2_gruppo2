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
        if not self.is_leaf(p):                                         # base case root position without children
                                                                        # nothing must be done since balance factor
                                                                        # is already 0.
            bf = self.retrieve_balance_factor(p)                        # save current balance factor in :var bf
            if self.left(p) is None and self.right(p) is not None:      # base case insert to the right
                # p._node._balance_factor = p._node._balance_factor - 1
                self.change_balance_factor(p, bf - 1)
                return
            elif self.right(p) is None and self.left(p) is not None:    # base case insert to the left
                # p._node._balance_factor = p._node._balance_factor + 1
                self.change_balance_factor(p, bf + 1)
                return
            elif self.retrieve_balance_factor(self.left(p)) == 0 \
                    and self.retrieve_balance_factor(self.right(p)) != 0:
                self.change_balance_factor(p, bf - 1)
                return
            elif self.retrieve_balance_factor(self.right(p)) == 0 \
                    and self.retrieve_balance_factor(self.left(p)) != 0:
                self.change_balance_factor(p, bf + 1)
                return
            elif self.retrieve_balance_factor(self.right(p)) == 0 \
                    and self.retrieve_balance_factor(self.left(p)) == 0:
                self.change_balance_factor(p, bf)
                return
            # elif self.left(p)._node._balance_factor == 0:               # trinode cases
            #      p._node._balance_factor = 0
            elif self.retrieve_balance_factor(self.left(p)) == 0:
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
        else:
            self.change_balance_factor(p, 0)

    def _isbalanced(self, p):
        return abs(self.retrieve_balance_factor(p)) <= 1

    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
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

    def _rebalance(self, p):
        while p is not None:
            if self.parent(p) is not None and self.is_balanced(p):
                self._recompute_balance_factor(self.parent(p))
            # old_balance_factor = self.retrieve_balance_factor(p)
            if not self.is_balanced(p):
                if not self.is_root(p):
                    old_balance_factor = self.retrieve_balance_factor(self.parent(p))
                else:
                    old_balance_factor = self.retrieve_balance_factor(p)
                # Enters if -2/+2 is detected
                p = self._restructure(self._tall_grandchild(p))
                # print(p.element()._key)
                # print(self.left(p).element()._key)
                # print(self.right(p).element()._key)
                self._recompute_balance_factor(self.left(p))
                self._recompute_balance_factor(self.right(p))
                #
                self._recompute_balance_factor(p)
                #
                # self._recompute_balance_factor(self.parent(p))
                if self.retrieve_balance_factor(p) == old_balance_factor:  # has height changed?
                    p = None  # no further changes needed
            else:
                p = self.parent(p)

    # ----------- methods for test purpose

    def is_balanced(self, p):
        return self._isbalanced(p)

