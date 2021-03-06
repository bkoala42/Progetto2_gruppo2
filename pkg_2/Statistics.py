from pkg_1.NewAVLTreeMap import NewAVLTreeMap
from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue


class Statistics:
    """
    The class elaborates statistics over a (key, value) data-set,
    using a NewAVLTreeMap whose nodes hold (key, frequency, total)
    elements. The complexity of the constructor is O(nlog(k))
    where n is the number of entries in the dataset, and k the
    number of different keys in the dataset.
    :param "key" is the key in the data-set
    :param "frequency" is equal to the number of occurrences of the
            key in the data-set
    :param "total" is equal to the sum of the values associated to
            all the occurrences of the key
    :__init__ takes in input the filename of the data-set
    """

    def __init__(self, fileName):
        # self.avl = NewAVLTreeMap()
        self.avl = NewAVLTreeMap()
        self.total = 0
        self.occur = 0
        try:
            file = open(fileName, "r")
        except FileNotFoundError:
            print("File not found")
        else:
            for line in file:
                if line == "empty":
                    break
                tmp = line.split(":")
                key = tmp[0]
                value = tmp[1]
                self.add(key, int(value))
            file.close()

    def add(self, k, v):
        """
        Adds the (k, v) couple to the map.
        If the key k is already inside the map, the method must update
        frequency and total fields associated to it accordingly. This
        method has complexity of log(k), where k is the number of
        different keys in the dataset.
        :param k: the key to add/update
        :param v: value associated to the key
        :return: empty
        The assumption taken is to store the parameters as follows:
            key = k
            value = list(frequency, total)
        Complexity O(logk)
        """
        if isinstance(k,str) and isinstance(v, int):
            tmp = []
            if k in self.avl:
                value = self.avl[k]
                frequency = value[0] + 1
                total = value[1] + v
                tmp.append(frequency)
                tmp.append(total)
            else:
                tmp.append(1)
                tmp.append(v)
            self.avl[k] = tmp
            self.occur = self.occur + 1
            self.total = self.total + v
        else:
            raise Exception("Type error: \nk must be a String\nv must be a integer  ")

    def len(self):
        """
        Returns the number of keys in the map in O(1) time.
        :return: the number of keys in the map
        """
        return len(self.avl)

    def occurrences(self):
        """
        Returns the number of occurences in the map in O(1) time.
        :return: Frequencies of the elements in the map.
        """
        return self.occur

    def average(self):
        """
        Returns the avarage of occurences in the map in O(1) time.
        :return: mean value of the values of the elements in the map.
        """
        return self.total / self.occurrences()

    def median(self):
        """
        Returns the median of the keys in the map in O(k) time.
        :return: median of the keys in the map
        """
        return self.percentile(50)

    def percentile(self, j):
        """
        Calculates the j-th percentile, for j = 1, ..., 99 of the lengths of keys,
        defined as the key k so that the j% of the occurrences of the data-set have
        keys with length smaller or equal to k
        Complexity at most O(k)
        :param j: index of the percentile
        :return: the j-th percentile
        """
        if self.len() != 0:
            if j > 100 or j < 0:
                raise Exception("j must be between [0:99]")
            else:
                if self.occurrences() % 2 == 0:
                    index = int((j * self.occurrences()) / 100)
                else:
                    index = int((j * self.occurrences()) / 100 + 1)
                tmp = 0
                for node in self.avl.items():
                    tmp = node[1][0] + tmp
                    if tmp >= index:
                        return node[0]
        else:
            if j == 50:
                raise Exception("AVL empty, no median available.")
            else:
                raise Exception("AVL empty, no percentile available.")

    def mostFrequent(self, j):
        """
        Returns a list containing the j-th most frequent keys.
        Complexity O(klogj) where k is the number of different
        keys.
        :param j: index of keys requested
        :return: j-most-frequent keys
        """
        if self.len() != 0:
            if j < 0:
                raise Exception("j must be positive")
            if j > self.len():
                j = self.len()

            queue = HeapPriorityQueue()

            for node in self.avl.items():
                if len(queue) < j:
                    queue.add(node[1][0], node[0])
                elif queue.min()[0] < node[1][0]:
                    queue.remove_min()
                    queue.add(node[1][0], node[0])

            list = []
            for i in range(j):
                list.append(queue.remove_min())
            return list
        else:
            raise Exception("The avl three is empty.")
