#from NewAVLTreeMap import NewAVLTreeMap
from sorted_priority_queue import SortedPriorityQueue
from TdP_collections.map.avl_tree import AVLTreeMap

class Statistics:

        def __init__(self, bool):
            #self.avl = NewAVLTreeMap()
            self.avl = AVLTreeMap()
            if bool:
            #If true, we can read from file
            #else, we have an AVL empty
                try:
                    file = open("prova.txt", "r")
                except FileNotFoundError:
                    print("File not found")
                else:
                    for line in file:
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
            else:
                tmp.append(1)
                tmp.append(v)
            self.avl[k] = tmp

        def len(self):
            """
            Returns the number of keys in the map in O(n) time, where n is the number of keys.
            :return: Number of keys in the map
            """
            return len(self.avl.keys())

        def occurrences(self):
            """
            Calculates the sum of the frequencies of the elements in the map by iteration in time O(n), where n is
            the number of the keys.
            :return: Sum of the frequences of the elements in the map.
            """
            value = self.avl.values()
            total = 0
            for i in value:
                total = total + i[0]
            return total

        def average(self):
            """
            Calculates the mean value of the values of the elements in the map by iteration in time O(n), where n is
            the number of the keys.
            :return: Mean value of the values of the elements in the map.
            """
            value = self.avl.values()
            total = 0
            for i in value:
                total = total + i[1]
            return total/self.len()

        def median(self):
            """
            NON SONO SICURO DELLA COMPLESSITA', VA RICALCOLATA CON ATTENZIONE
            Calculates the central key of the set of keys taking into account their frequency in time O(k) where k is
            the number of the occurrences in the dataset.
            :return: Median of the keys in the map.
            """
            if self.len() == 0:
                # if the map is empty no median available
                return None, None
            else:
                tmp = []
                for node in self.avl:
                    #for each node fill an array with the occurrences
                    frequency = self.avl.get(node)[0]
                    if len(tmp) == 0:
                        tmp = [node] * frequency
                    else:
                        tmp1 = [node] * frequency
                        tmp.extend(tmp1)
                if len(tmp) % 2 == 1:
                    # if even number of occurrences return the exact central values
                    return tmp[int(len(tmp)/2)],None
                else:
                    # if odd number of occurences return the two values in the middle of the array
                    return tmp[int(len(tmp)/2)], tmp[int(len(tmp)/2 + 1)]

        def percentile(self, j = 20):
            tmp = []
            if j > 100:
                raise Exception("j must be between [0:99]")
            else:
                for node in self.avl:
                    frequency = self.avl.get(node)[0]
                    if len(tmp) == 0:
                        tmp = [node] * frequency
                    else:
                        tmp1 = [node] * frequency
                        tmp.extend(tmp1)
            return tmp[int((len(tmp)*j)/100)-1]

        def mostFrequent(self, j):
            if self.len() == 0:
                return None
            if (j > self.len()):
                j = self.len()
            list = []
            queue = SortedPriorityQueue()
            for node in self.avl:
                queue.add(self.avl.get(node)[0], node)
            for i in range(j):
                list.append(queue.remove_max()[1])
            return list
