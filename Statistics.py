#from NewAVLTreeMap import NewAVLTreeMap 
from sorted_priority_queue import SortedPriorityQueue
from TdP_collections.map.avl_tree import AVLTreeMap

class Statistics:

        def __init__(self):
            #self.avl = NewAVLTreeMap()
            self.avl = AVLTreeMap()
            try:
                file = open("prova.txt", "r")
            except FileNotFoundError:
                print("File not found")
            else:
                while 1:
                    line = file.readline()
                    if not line:
                        break
                    tmp = line.split(":")
                    key = tmp[0]
                    value = tmp[1]
                    self.add(key, int(value))

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
            if self.len() == 0:
                return None, None
            else:
                tmp = []
                for node in self.avl:
                    frequency = self.avl.get(node)[0]
                    if len(tmp) == 0:
                        tmp = [node] * frequency
                    else:
                        tmp1 = [node] * frequency
                        tmp.extend(tmp1)
                lenght = len(tmp)
                if lenght % 2 == 1:
                    return tmp[int(lenght/2)],None
                else:
                    return tmp[int(lenght/2)], tmp[int(lenght/2 + 1)]

        def percentile(self, j):
            tmp = []
            if j <0 or j > 100:
                raise Exception("j must be between [0:99]")
            else:
                for node in self.avl:
                    frequency = self.avl.get(node)[0]
                    if len(tmp) == 0:
                        tmp = [node] * frequency
                    else:
                        tmp1 = [node] * frequency
                        tmp.extend(tmp1)
            return tmp[int((len(tmp)*j)/100)]

        def mostFrequent(self, j):
            if (j > self.len()):
                j = self.len()
            list = []
            queue = SortedPriorityQueue()
            for node in self.avl:
                queue.add(self.avl.get(node)[0], node)
            for i in range(j):
                list.append(queue.remove_max()[1])
            return list
