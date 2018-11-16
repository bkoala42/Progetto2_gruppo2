from TdP_collections.map.avl_tree import AVLTreeMap

class Statistics:

        def __init__(self, TreeMap):
            self.avl = AVLTreeMap(TreeMap)
            try:
                file = open("prova.txt", "r")
            except FileNotFoundError:
                print("File non trovato")
            else:
                while 1:
                    line = file.readline()
                    if not line:
                        break
                    tmp = line.split(":")
                    key = tmp[0]
                    value = tmp[1]
                    self.add(key, value)

        def add(self, k, v):
            tmp = []
            if k in self.avl.keys():
                value = self.avl.get(k)
                frequency = value[0] + 1
                total = value[1] + v
                tmp.append(frequency)
                tmp.append(total)
                self.avl[k] = tmp
            else:
                tmp.append(1)
                tmp.append(v)
                self.avl[k] = tmp

        def len(self):
            return len(self.avl.keys())

        def occurrences(self):
            value = self.avl.values()
            total = 0
            for i in value:
                total = total + i[0]
            return total

        def average(self):
            value = self.avl.values()
            total = 0
            for i in value:
                total = total + i[1]
            return total/self.len()

        def median(self):
            """ TODO """
            pass

