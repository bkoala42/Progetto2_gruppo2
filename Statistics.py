from TdP_collections.map.avl_tree import AVLTreeMap

class Statistics:

        def __init__(self, TreeMap):
            self.avl = AVLTreeMap(TreeMap)


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


