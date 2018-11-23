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

        def right_height(self):
            pass

    def _retrieve_balance_factor(self, p):
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

    def _change_balance_factor(self, p, v):
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

    def _recompute_balance_factor(self, p, bf_grandchild, rotation_type):
        """
             B
            / \
           A   C
        :param p: B the root of restructured tree
        :param bf_grandchild: balance factor of B BEFORE RESTRUCTURE
        :param rotation_type: type of rotation
        :raise ValueError
        """
        left = self.left(p)
        right = self.right(p)

        if rotation_type == 0:
            # RR case -> Left rotation has been performed
            if self._retrieve_balance_factor(p) == 0:
                self._change_balance_factor(left, -1)
                self._change_balance_factor(p, 1)
            # elif bf_grandchild == -1:
            else:
                self._change_balance_factor(left, 0)
                self._change_balance_factor(p, 0)
        elif rotation_type == 1:
            # LL case -> Right rotation has been performed
            if self._retrieve_balance_factor(p) == 0:
                self._change_balance_factor(right, 1)
                self._change_balance_factor(p, -1)
            else:
                self._change_balance_factor(right, 0)
                self._change_balance_factor(p, 0)
        elif rotation_type == 2:
            self._change_balance_factor(p, 0)
            if bf_grandchild == 0:
                self._change_balance_factor(right, 0)
                self._change_balance_factor(left, 0)
            elif bf_grandchild == -1:
                self._change_balance_factor(right, 0)
                self._change_balance_factor(left, 1)
            elif bf_grandchild == 1:
                self._change_balance_factor(right, -1)
                self._change_balance_factor(left, 0)
            else:
                raise ValueError("Not balanced Tree")
        else:
            raise ValueError("Unavailable Type")

    def _update_balance_factor_delete(self, p):
        """
        Since delete calls rebalance on the parent thus losing the link with the old child,
        we need to evaluate and update the balance factor before calling the rebalance. This
        can be achieved by checking base cases, that are:
            leaf in the following level
            deleting one element of the level (left None / right None)
            leaves in a level below
            only one leaf in a level below (left None / right None)
        :param p: position passed by the delete, that is always the parent of the deleted node
        """
        if self.is_leaf(p):
            self._change_balance_factor(p, 0)
        elif self.left(p) is None:
            self._change_balance_factor(p, self._retrieve_balance_factor(p) - 1)
        elif self.right(p) is None:
            self._change_balance_factor(p, self._retrieve_balance_factor(p) + 1)

        elif self.is_leaf(self.left(p)) and self.is_leaf(self.right(p)):
            self._change_balance_factor(p, 0)
        elif self.is_leaf(self.left(p)):
            self._change_balance_factor(p, self._retrieve_balance_factor(p) - 1)
        elif self.is_leaf(self.right(p)):
            self._change_balance_factor(p, self._retrieve_balance_factor(p) + 1)

    def _isbalanced(self, p):
        """
        A node (inside a position p) is considered to be balanced iff its balance factor is equal
        to -1, 0, 1
        :param p: position to evaluate
        """
        return abs(self._retrieve_balance_factor(p)) <= 1

    # Per valutare i fattori di bilanciamento per le operazioni di insert e delete
    # necessitiamo di conoscere il tipo di rotazione effettuata (derivante dal caso
    # di sbilanciamento RR, LL, RL, LR). Quindi:
    #       RR      -> singola rotazione a sinistra
    #       LL      -> singola rotazione a destra
    #       RL/LR   -> doppia rotazione

    def _tall_child(self, p, favorleft=False) -> (Position, bool):
        """
        Returns the tallest child node and a boolean to indicate if it is the left child or right child
        :param p: father position
        :param favorleft: favor left default param
        :return: tallest child, is_left
        """
        # _ = self._validate(p)
        if (self._retrieve_balance_factor(p) == 0 and favorleft) or self._retrieve_balance_factor(p) > 0:
            return self.left(p), True
        elif self._retrieve_balance_factor(p) <= 0:
            return self.right(p), False

    def _tall_grandchild(self, p) -> (Position, int):
        """
        Returns the tallest granchild node and the type of rotation performed
        :param p: grandfather position
        :return: tallest child, 0/1/2 for RR/LL/RL or LR
        """
        child_node, child_is_left = self._tall_child(p)
        # If child is on left, favor left grandchild; else favor right grandchild
        alignment = (child_node == self.left(p))
        grandchild_node, grandchild_is_left = self._tall_child(child_node, alignment)
        if child_is_left==grandchild_is_left and grandchild_is_left:
            rotation_type = 1
        elif grandchild_is_left==child_is_left:
            rotation_type = 0
        else:
            rotation_type = 2
        return grandchild_node, rotation_type

    def _rebalance(self, p, insert):
        """
        Rebalance avl starting from parent(p)
        :param p:
        :param insert: bool indicating insert (True) or delete (False) operation
        """
        current = self.parent(p)
        while current is not None:
            # Sto ribilanciando salendo da sinistra o destra -> aggiorno fattori di bilanciamento
            if (self.left(current) == p and insert) or (self.right(current) == p and not insert):
                self._change_balance_factor(current, self._retrieve_balance_factor(current) + 1)
            else:
                self._change_balance_factor(current, self._retrieve_balance_factor(current) - 1)

            if not self._isbalanced(current):
                child, type_of_rotation = self._tall_grandchild(current)
                current = self._restructure(child)
                self._recompute_balance_factor(current, self._retrieve_balance_factor(child), type_of_rotation)

            # Stop conditions
            if (self._retrieve_balance_factor(current) == 0 and insert) or (
                    abs(self._retrieve_balance_factor(current)) == 1 and not insert):
                current = None
            else:
                p = current
                current = self.parent(p)

    # ---------------------------- override balancing hooks ----------------------------

    def _rebalance_insert(self, p):
        self._rebalance(p, True)

    def _rebalance_delete(self, p):
        if p is not None:
            self._update_balance_factor_delete(p)

            # Restructure is needed
            if not self._isbalanced(p):
                g_child, type_of_rotation = self._tall_grandchild(p)
                p = self._restructure(g_child)
                self._recompute_balance_factor(p, self._retrieve_balance_factor(g_child), type_of_rotation)

            if self._retrieve_balance_factor(p) == 0:
                self._rebalance(p, False)

    # ---------------------------- methods for test purpose ----------------------------

    def retrieve_balance_factor(self, p):
        """
        :param p: position
        :return: balance factor associated to the node inside the position
        """
        return p.get_node().get_balance_factor()