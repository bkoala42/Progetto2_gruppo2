from pkg_1.NewAVLTreeMap import NewAVLTreeMap
from TdP_collections.map.avl_tree import AVLTreeMap


def test_insert_awl_map():
    """
    Testing insert using inherited methods
    """
    t = NewAVLTreeMap()
    t[42] = "Armando"
    if t.root() is not None and t[42] == "Armando":
        print("Test test_insert_awl_map passed")
    else:
        print("Test test_insert_awl_map failed")


def test_delete_awl_map():
    """
    Testing delete using inherited methods
    """
    t = NewAVLTreeMap()
    t[42] = "Armando"
    t[3] = "Marco"
    del t[42]
    if t.root() is not None and t.root().element()._key == 3:
        print("Test test_delete_awl_map passed")
    else:
        print("Test test_delete_awl_map failed")


def test_rr_rotation_insert():
    """
    This unbalanced case is resolved by performing a single left rotation
    """
    t = NewAVLTreeMap()
    old_t = AVLTreeMap()
    #
    # #
    # #     2    FB = -2                17     FB = 0
    # #      \                        /   \
    # #       17  FB = -1    ->      2     42  FB = 0
    # #        \
    # #         42    FB = 0
    #
    #
    t[2], old_t[2] = 2, 2
    t[17], old_t[17] = 17, 17
    t[42], old_t[42] = 42, 42
    if t.retrieve_balance_factor(t.root()) == 0 and \
            t.root().element()._key == 17 and \
            t.left(t.root()).element()._key == 2 and \
            t.right(t.root()).element()._key == 42 and \
            old_t.root().element()._key == 17 and \
            old_t.left(old_t.root()).element()._key == 2 and \
            old_t.right(old_t.root()).element()._key == 42:
        print("Test test_rr_rotation_insert passed")
    else:
        print("Test test_rr_rotation_insert failed")


def test_ll_rotation_insert():
    """
    This unbalance case is resolved by performing a single right rotation
    """
    t = NewAVLTreeMap()
    old_t = AVLTreeMap()
    #
    # #
    # #       42    FB = 2               17     FB = 0
    # #      /                         /   \
    # #     17      FB = 1    ->      9     42  FB = 0
    # #     /
    # #    9        FB = 0
    #
    #
    t[42], old_t[42] = 42, 42
    t[17], old_t[17] = 17, 17
    t[9], old_t[9] = 9, 9
    if t.retrieve_balance_factor(t.root()) == 0 and \
            t.root().element()._key == 17 and \
            t.left(t.root()).element()._key == 9 and \
            t.right(t.root()).element()._key == 42 and \
            old_t.root().element()._key == 17 and \
            old_t.left(old_t.root()).element()._key == 9 and \
            old_t.right(old_t.root()).element()._key == 42:
        print("Test test_ll_rotation_insert passed")
    else:
        print("Test test_ll_rotation_insert failed")


def test_lr_rotation_insert():
    """
    This unbalance case is resolved by performing 1) a left rotation 2) a right rotation
    """
    t = NewAVLTreeMap()
    old_t = AVLTreeMap()
    #
    # #
    # #       42        FB = 2               42            35           FB = 0
    # #      /                              /             /  \
    # #     17          FB = -1    ->      35       ->   17   42        FB = 0
    # #      \                            /
    # #       35        FB = 0           17
    #
    #
    t[42], old_t[42] = 42, 42
    t[17], old_t[17] = 17, 17
    t[35], old_t[35] = 35, 35
    if t.retrieve_balance_factor(t.root()) == 0 and \
            t.root().element()._key == 35 and \
            t.left(t.root()).element()._key == 17 and \
            t.right(t.root()).element()._key == 42 and \
            old_t.root().element()._key == 35 and \
            old_t.left(old_t.root()).element()._key == 17 and \
            old_t.right(old_t.root()).element()._key == 42:
        print("Test test_lr_rotation_insert passed")
    else:
        print("Test test_lr_rotation_insert failed")


def test_rl_rotation_insert():
    """
    This unbalance case is resolved by performing 1) a right rotation 2) a left rotation
    """
    t = NewAVLTreeMap()
    old_t = AVLTreeMap()
    #
    # #
    # #       3         FB = -2           3                4        FB = 0
    # #        \                           \              / \
    # #         42      FB = 1    ->        4      ->    3   42     FB = 0
    # #        /                             \
    # #       4         FB = 0                42
    #
    #
    t[3], old_t[3] = 3, 3
    t[42], old_t[42] = 42, 42
    t[4], old_t[4] = 4, 4
    if t.retrieve_balance_factor(t.root()) == 0 and \
            t.root().element()._key == 4 and \
            t.left(t.root()).element()._key == 3 and \
            t.right(t.root()).element()._key == 42 and \
            old_t.root().element()._key == 4 and \
            old_t.left(old_t.root()).element()._key == 3 and \
            old_t.right(old_t.root()).element()._key == 42 and \
            t.retrieve_balance_factor(t.left(t.root())) == 0 and \
            t.retrieve_balance_factor(t.right(t.root())) == 0:
        print("Test test_rl_rotation_insert passed")
    else:
        print("Test test_rl_rotation_insert failed")


def test_dense_tree_balance_factor():
    """
    Testing the correctness of balance factors after many inserts
    """
    t = NewAVLTreeMap()
    #
    # #
    # #       3         FB = -2           4        FB = 0         4
    # #        \                         / \                    /   \
    # #         42      FB = 1    ->   3   42     FB = 0   -> 3     42     ->
    # #        /                                                    / \
    # #       4         FB = 0                                    10  55
    #                                                             /
    #                                                            6
    #
    #                    10            FB = 1
    #                   /  \
    #  FB = -1         4    42         FB = -1
    #                 / \     \
    #  FB = 0,  1    3   6     55      FB = 0
    #                   /
    #  FB = 0          5

    t[3] = 3
    t[42] = 42
    t[4] = 4
    t[55] = 55
    t[10] = 10
    t[6] = 6
    t[5] = 5
    # for i in t:
    #     print("element: {}".format(i))
    if (
            # FB(10) = 1
            t.retrieve_balance_factor(t.root()) == 1 and t.root().element()._key == 10 and
            # FB(4) = -1
            t.retrieve_balance_factor(t.left(t.root())) == -1 and t.left(t.root()).element()._key == 4 and
            # FB(42) = -1
            t.retrieve_balance_factor(t.right(t.root())) == -1 and t.right(t.root()).element()._key == 42 and
            # FB(55) = 0
            t.retrieve_balance_factor(t.right(t.right(t.root()))) == 0 and t.right(t.right(
                                                                            t.root())).element()._key == 55 and
            # FB(6) = 1
            t.retrieve_balance_factor(t.right(t.left(t.root()))) == 1 and t.right(t.left(t.root())).element()._key == 6 and
            # FB(3) = 0
            t.retrieve_balance_factor(t.left(t.left(t.root()))) == 0 and t.left(t.left(t.root())).element()._key == 3 and
            # FB(5) = 0
            t.retrieve_balance_factor(t.left(t.right(t.left(t.root())))) == 0 and
                                        t.left(t.right(t.left(t.root()))).element()._key == 5
    ):
        print("Test test_dense_tree_balance_factor passed")
    else:
        print("Test test_dense_tree_balance_factor failed")


def test_ll_rotation_delete():
    """
    This unbalanced case is resolved by performing a single right rotation
    """
    t = NewAVLTreeMap()
    t[10] = 10
    t[4] = 4
    t[42] = 42
    t[3] = 3
    #
    # #
    # #      10      FB = 1         10             4
    # #     /  \                   /              / \
    # #    4    42   FB = 0   ->  4       ->     3  10
    # #   /                      /
    # #  3                      3
    # #
    #
    del t[42]
    # print(t.retrieve_balance_factor(t.root()))
    if t.retrieve_balance_factor(t.root()) == 0 and \
            t.root().element()._key == 4 and \
            t.left(t.root()).element()._key == 3 and \
            t.right(t.root()).element()._key == 10:
        print("Test test_ll_rotation_delete passed")
    else:
        print("Test test_ll_rotation_delete failed")


def test_rr_rotation_delete():
    """
    This unbalanced case is resolved by performing a single left rotation
    """
    t = NewAVLTreeMap()
    t[4] = 10
    t[10] = 10
    t[3] = 3
    t[42] = 42
    #
    # #
    # #      4      FB = -1         4                10
    # #     / \                      \              /  \
    # #    3   10   FB = -1   ->      10      ->   4    42
    # #          \                     \
    # #          42 FB = 0              42
    # #
    #
    del t[3]
    # print(t.retrieve_balance_factor(t.root()))
    if t.retrieve_balance_factor(t.root()) == 0 and \
            t.root().element()._key == 10 and \
            t.left(t.root()).element()._key == 4 and \
            t.right(t.root()).element()._key == 42:
        print("Test test_rr_rotation_delete passed")
    else:
        print("Test test_rr_rotation_delete failed")


def test_lr_rotation_delete():
    """
    This unbalanced case is resolved by performing 1) a left rotation 2) a right rotation
    """
    t = NewAVLTreeMap()
    t[42] = 42
    t[5] = 5
    t[50] = 50
    t[10] = 10
    #
    # #
    # #      42      FB = 1              42           42         10
    # #     /  \                        /            /          /  \
    # #    5    50   FB = -1, 0    ->  5      ->    10    ->   5    42
    # #     \                           \          /
    # #      10      FB = 0              10       5
    # #
    #
    del t[50]
    # print(t.retrieve_balance_factor(t.root()))
    if t.retrieve_balance_factor(t.root()) == 0 and \
            t.root().element()._key == 10 and \
            t.left(t.root()).element()._key == 5 and \
            t.right(t.root()).element()._key == 42:
        print("Test test_lr_rotation_delete passed")
    else:
        print("Test test_lr_rotation_delete failed")


def test_rl_rotation_delete():
    """
    This unbalanced case is resolved by performing 1) a right rotation 2) a left rotation
    """
    t = NewAVLTreeMap()
    t[10] = 10
    t[5] = 5
    t[42] = 42
    t[35] = 35
    #
    # #
    # #      10      FB = -1          10        10             35
    # #     /  \                       \         \            /  \
    # #    5    42   FB = 0, 1    ->    42  ->    35  ->     10   42
    # #        /                       /           \
    # #       35     FB = 0           35            42
    # #
    #
    del t[5]
    # print(t.retrieve_balance_factor(t.root()))
    if t.retrieve_balance_factor(t.root()) == 0 and \
            t.root().element()._key == 35 and \
            t.left(t.root()).element()._key == 10 and \
            t.right(t.root()).element()._key == 42:
        print("Test test_rl_rotation_delete passed")
    else:
        print("Test test_rl_rotation_delete failed")


def test_multiple_insert_delete():
    """
    This test verifies the correctness of avl properties after multiple insert and delete operations
    """
    t = NewAVLTreeMap()
    t[10] = 10
    t[5] = 5
    t[42] = 42
    t[35] = 35
    t[12] = 12
    t[33] = 33
    del t[12]
    del t[35]
    t[3] = 3
    t[56] = 56
    t[44] = 44
    t[43] = 43
    t[32] = 32
    t[39] = 39
    del t[5]
    del t[42]
    t[42] = 42
    t[14] = 14
    t[13] = 13
    t[12] = 12
    t[6] = 6
    t[2] = 2
    t[1] = 1

    index=0
    list_to_check = [39, 10, 44, 3, 14, 43, 56, 2, 6, 13, 32, 42, 1, 12, 33]
    if t.retrieve_balance_factor(t.root()) == 1:
        for x in t.breadthfirst():
            if x.element()._key != list_to_check[index]:
                print("Test test_multiple_insert_delete failed")
                return
            index += 1
        print("Test test_multiple_insert_delete passed")


def run_test_new_awl():
    test_insert_awl_map()
    test_delete_awl_map()
    test_rr_rotation_insert()
    test_ll_rotation_insert()
    test_lr_rotation_insert()
    test_rl_rotation_insert()
    test_dense_tree_balance_factor()
    test_ll_rotation_delete()
    test_rr_rotation_delete()
    test_lr_rotation_delete()
    test_rl_rotation_delete()
    test_multiple_insert_delete()


if __name__ == "__main__":
    run_test_new_awl()
