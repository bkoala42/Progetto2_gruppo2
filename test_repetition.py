from repetitions import find_repetition

""" In order to test this utility it is necessary to create two directories with ONLY files. One with duplicated
    files with both equal names and different names, and one without duplicated files."""

def test_find_repetition_collide():
    dir = "DIRECTORY WITH DUPLICATES"
    collides = find_repetition(dir)
    #add to this condition the name of the duplicate files
    if len(collides) != 0:
        print("Test test_find_repetition_collide passed")
    else:
        print("Test test_find_repetition_collide failed")


def test_find_repetition_no_collide():
    dir = "DIRECTORY WITHOUT DUPLICATES"
    collides = find_repetition(dir)
    if len(collides) == 0:
        print("Test test_find_repetition_collide passed")
    else:
        print("Test test_find_repetition_collide failed")