from os import listdir

def find_repetition(directory):
    """
    Finds duplicate files by checking if the hash of their contents collide. Computational complexity O(n) where n is
    the number of files in the directory.
    :param directory: Directory in which check for duplicated files
    :return: List of duplicated files
    """
    table = {}
    colliding = {}
    files = listdir(directory)
    for file in files:
        try:
            file_content = open(directory+"\\"+file).read()
            if hash(file_content) in table.keys():
                tmp = colliding.get(table[hash(file_content)])
                tmp.append(file)
                colliding[table[hash(file_content)]] = tmp
            else:
                table[hash(file_content)] = file
                colliding[file] = []
        except Exception as e:
            print(e)
    return colliding
