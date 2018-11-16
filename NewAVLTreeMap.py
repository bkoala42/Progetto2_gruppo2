from TdP_collections.map.avl_tree import AVLTreeMap
from TdP_collections.map.avl_tree import TreeMap


class NewAVLTreeMap(AVLTreeMap):
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing.

        We use convention that a "None" child has height 0, thus a leaf has height 1.
        """
        __slots__ = '_rebalance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._rebalance_factor = 0

        def get_rebalance_factor(self):
            return self._rebalance_factor

        def left_height(self):
            pass
            # return self._left._height if self._left is not None else 0

        def right_height(self):
            pass
            # return self._right._height if self._right is not None else 0

    def _compute_height(self, p):
        return self.height(p)

    def _recompute_rebalance_factor(self, p):
        # caso base inserimento a dx e sx
        if not self.is_leaf(p):
            if self.left(p) == None and self.right(p) != None:
                p._node._rebalance_factor = p._node._rebalance_factor - 1
            elif self.right(p) == None and self.left(p) != None:
                p._node._rebalance_factor = p._node._rebalance_factor + 1
            # casi trinode vedi quaderno
            elif self.left(p)._node._rebalance_factor == 0:
                p._node._rebalance_factor = 0
            elif self.left(p)._node._rebalance_factor == -1:
                p._node._rebalance_factor = 1
            elif self.left(p)._node._rebalance_factor == 1:
                p._node._rebalance_factor = -1
            elif self.right(p)._node._rebalance_factor == 0:
                p._node._rebalance_factor = 0
            elif self.right(p)._node._rebalance_factor == -1:
                p._node._rebalance_factor = 1
            elif self.left(p)._node._rebalance_factor == 1:
                p._node._rebalance_factor = -1
        # va un più da qualche parte


    def _isbalanced(self, p):
        return abs(p._node._rebalance_factor) <= 1

    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
        # esiste il caso -2/+2???
        if p._node._rebalance_factor == 0 and favorleft:
            return self.left(p)
        elif p._node._rebalance_factor > 0:
            return self.left(p)
        elif p._node._rebalance_factor < 0:
            return self.right(p)
        #else:
        #    return self.right(p)

    def _rebalance(self, p):
        while p is not None:
            if self.parent(p) is not None:
                self._recompute_rebalance_factor(self.parent(p))
            old_rebalance_factor = p._node._rebalance_factor
            if not self.is_balanced(p):
                p = self._restructure(self._tall_grandchild(p))
                print(p.element()._key)
                print(self.left(p).element()._key)
                print(self.right(p).element()._key)
                self._recompute_rebalance_factor(self.left(p))
                self._recompute_rebalance_factor(self.right(p))
                self._recompute_rebalance_factor(p)
                #self._recompute_rebalance_factor(self.parent(p))
                if p._node._rebalance_factor == old_rebalance_factor:  # has height changed?
                    p = None  # no further changes needed
            else:
                p = self.parent(p)

    # ----------- methods for test purpose

    def is_balanced(self, p):
        return self._isbalanced(p)

