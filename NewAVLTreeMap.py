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

        def left_height(self):
            pass
            # return self._left._height if self._left is not None else 0

        def right_height(self):
            pass
            # return self._right._height if self._right is not None else 0

    def _compute_height(self, p):
        return self.height(p)

    def _recompute_rebalance_factor(self, p):
        p._node._rebalance_factor = self.height(self.left(p)) - self.height(self.right(p))

    def _isbalanced(self, p):
        return abs(p._node._rebalance_factor) <= 1

    def is_balanced(self, p):
        return self._isbalanced(p)

    def _tall_child(self, p, favorleft=False):  # parameter controls tiebreaker
        # esiste il caso -2/+2???
        if p._node._rebalance_factor == 0 and favorleft:
            return self.left(p)
        elif p._node._rebalance_factor == 1:
            return self.right(p)
        elif p._node._rebalance_factor == -1:
            return self.left(p)
        else:
            return self.right(p)

    def _rebalance(self, p):
        while p is not None:
            old_rebalance_factor = p._node._rebalance_factor  # trivially 0 if new node
            if not self._isbalanced(p):  # imbalance detected!
                # perform trinode restructuring, setting p to resulting root,
                # and recompute new local heights after the restructuring
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_rebalance_factor(self.left(p))
                self._recompute_rebalance_factor(self.right(p))
            self._recompute_rebalance_factor(p)  # adjust for recent changes
            if p._node._rebalance_factor == old_rebalance_factor:  # has height changed?
                p = None  # no further changes needed
            else:
                # parent è rotto???
                p = self.parent(p)