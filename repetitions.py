from os import listdir

def find_repetition(dir):
    table = {}
    colliding = []
    files = listdir(dir)
    for file in files:
        file_content = open(file, "r").read()
        if hash(file_content) in table.keys():
            colliding.append(file)
        else:
            table[hash(file_content)] = file
    return colliding


