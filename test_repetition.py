from repetitions import find_repetition

""" In order to test this utility it is necessary to create two directories with ONLY text files. One with duplicated
    files with both equal names and different names, and one without duplicated files."""


def test_find_repetition_collide():
    """ Tests find_repetition in case of directory with duplicated files. """
    dir_test = "Colliding"
    collides = find_repetition(dir_test)
    k = 0
    for i in collides.keys():
        if len(collides[i]) == 0 and collides[i] == []:
            k = k + 1
            continue
        if len(collides[i]) == 2 and collides[i] == ['File3.txt', 'File5.txt']:
            k = k + 1
            continue
        if len(collides[i]) == 0 and collides[i] == []:
            k = k + 1
            continue
    if len(collides.keys()) == k:
        print("Test test_find_repetition_collide passed")
    else:
        print("Test test_find_repetition_collide failed")


def test_find_repetition_multiple_collide():
    """ Tests find_repetition in case of directory with more than one duplicated files. """
    dir_test = "MultipleColliding"
    collides = find_repetition(dir_test)
    k = 0
    for i in collides.keys():
        if len(collides[i])  == 1 and collides[i] == ['File6.txt']:
            k = k +1
        if len(collides[i]) == 2 and collides[i] == ['File3.txt', 'File5.txt']:
            k = k + 1
        if len(collides[i]) == 0 and collides[i] == []:
            k = k + 1
        if len(collides[i]) == 1 and collides[i] == ['File8.txt']:
            k = k +1
    if k == len(collides.keys()):
        print("Test test_find_repetition_multiple_collide passed")
    else:
        print("Test test_find_repetition_multiple_collide failed")

def test_find_repetition_no_collide():
    """ Tests find_repetition in case of directory without duplicated files. """
    dir_test = "NotColliding"
    collides = find_repetition(dir_test)
    for i in collides.keys():
        if len(collides[i]) != 0:
            print("Test test_find_repetition_no_collide failed")
            break
    print("Test test_find_repetition_no_collide passed")

def run_test_repetition():
    test_find_repetition_collide()
    test_find_repetition_no_collide()
    test_find_repetition_multiple_collide()


if __name__ == "__main__":
    run_test_repetition()
