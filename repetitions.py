from os import listdir, getcwd, chdir


def find_repetition(directory):
    """
    Finds duplicate files by checking if the hash of their contents collide. Computational complexity O(n) where n is
    the number of files in the directory.
    :param directory: Directory in which check for duplicated files
    :return: List of duplicated files
    """
    table = {}
    colliding = []
    files = listdir(directory)
    for file in files:
        try:
            file_content = open(directory+"\\"+file).read()
            if hash(file_content) in table.keys():
                if table[hash(file_content)] not in colliding:
                    colliding.append(table[hash(file_content)])
                colliding.append(file)
            else:
                table[hash(file_content)] = file
        except Exception as e:
            print(e)
    return colliding





