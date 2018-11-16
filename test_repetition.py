from repetitions import find_repetition

""" In order to test this utility it is necessary to create two directories with ONLY text files. One with duplicated
    files with both equal names and different names, and one without duplicated files."""

def test_find_repetition_collide():
    """ Tests find_repetition in case of directory with duplicated files. """
    dir_test = "Colliding"
    collides = find_repetition(dir_test)
    #add to this condition the name of the duplicate files
    if len(collides) != 0 and 'File2.txt' in collides and 'File3.txt' in collides and 'File5.txt' in collides:
        print("Test test_find_repetition_collide passed")
    else:
        print("Test test_find_repetition_collide failed")

def test_find_repetition_multiple_collide():
    """ Tests find_repetition in case of directory with more than one duplicated files. """
    dir_test = "MultipleColliding"
    collides = find_repetition(dir_test)
    #add to this condition the name of the duplicate files
    if len(collides) != 0 and 'File2.txt' in collides and 'File3.txt' in collides and 'File5.txt' in collides \
            and 'File1.txt' in collides and 'File6.txt' in collides:
        print("Test test_find_repetition_multiple_collide passed")
    else:
        print("Test test_find_repetition_multiple_collide failed")


def test_find_repetition_no_collide():
    """ Tests find_repetition in case of directory without duplicated files. """
    dir_test = "NotColliding"
    collides = find_repetition(dir_test)
    if len(collides) == 0:
        print("Test test_find_repetition_no_collide passed")
    else:
        print("Test test_find_repetition_no_collide failed")


test_find_repetition_collide()
test_find_repetition_no_collide()
test_find_repetition_multiple_collide()
