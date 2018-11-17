# from NewAVLTreeMap import NewAVLTreeMap
from sorted_priority_queue import SortedPriorityQueue
from TdP_collections.map.avl_tree import AVLTreeMap


class Statistics:
    """
    The class elaborates statistics over a (key, value) data-set,
    using a NewAVLTreeMap whose nodes hold (key, frequency, total)
    elements.
    :param "key" is the key in the data-set
    :param "frequency" is equal to the number of occurrences of the
            key in the data-set
    :param "total" is equal to the sum of the values associated to
            all the occurrences of the key
    :__init__ takes in input the filename of the data-set
    """

    def __init__(self, bool):
        # self.avl = NewAVLTreeMap()
        self.avl = AVLTreeMap()
        if bool:
            # If true, the class reads data from file
            # else, we have an empty AVL tree map
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
        """
        Adds the (k, v) couple to the map.
        If the key k is already inside the map, the method must update
        frequency and total fields associated to it accordingly.
        :param k: the key to add/update
        :param v: value associated to the key
        The assumption taken is to store the parameters as follows:
            key = k
            value = list(frequency, total)
        TODO CHECK COMPLEXITY
        The method takes O(1) to search in keys() method for python 3.x
        and insertion takes O(1) (based on python documentation).
        """
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
        Returns the number of keys in the map in O(n) time, where n is
        the number of the keys.
        :return: the number of keys in the map
        """
        return len(self.avl.keys())

    def occurrences(self):
        """
        Calculates the sum of the frequencies of the elements in the map
        by iterating in time O(n), where n is the number of the keys.
        :return: Sum of the frequencies of the elements in the map.
        """
        value = self.avl.values()
        """ :var value is a list containing (frequency, total) """
        total_frequencies = 0
        for i in value:
            total_frequencies = total_frequencies + i[0]
        return total_frequencies

    def average(self):
        """
        Calculates the mean value of the values of the occurrences in the
        map by iterating in time O(n), where n is the number of the keys.
        :return: mean value of the values of the elements in the map.
        """
        value = self.avl.values()
        """ :var value is a list containing (frequency, total) """
        mean_value = 0
        for i in value:
            mean_value = mean_value + i[1]
        return mean_value / self.len()      # TODO what the fuck

    def median(self):
        """
        TODO CHECK COMPLEXITY
        Calculates the central key of the set of keys taking into account
        their frequency in time O(k) where k is the number of the occurrences
        in the data-set.
        :return: median of the keys in the map as a tuple   #TODO si puo' fare senza tupla?
        """
        if self.len() == 0:
            # if the map is empty no median available
            return None, None
        else:
            tmp = []
            for node in self.avl:
                # for each node fill an array with the occurrences
                frequency = self.avl.get(node)[0]
                if len(tmp) == 0:
                    tmp = [node] * frequency
                else:
                    tmp1 = [node] * frequency
                    tmp.extend(tmp1)        # TODO why extend?
            if len(tmp) % 2 == 1:
                # if even number of occurrences return the exact central values
                return tmp[int(len(tmp) / 2)], None
            else:
                # if odd number of occurrences return the two values in the middle of the array
                return tmp[int(len(tmp) / 2)], tmp[int(len(tmp) / 2 + 1)]

    def percentile(self, j=20):
        """
        Calculates the j-th percentile, for j = 1, ..., 99 of the lengths of keys,
        defined as the key k so that the j% of the occurrences of the data-set have
        keys lower or equal to k
        :param j: index of the percentile
        :return: the j-th percentile
        """
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
        return tmp[int((len(tmp) * j) / 100) - 1]

    def mostFrequent(self, j):
        """
        Returns a list containing the j-th most frequent keys.
        :param j: index of keys requested
        :return: j-most-frequent keys
        """
        if self.len() == 0:
            return None
        if j > self.len():
            j = self.len()
        list = []
        queue = SortedPriorityQueue()
        for node in self.avl:
            queue.add(self.avl.get(node)[0], node)
        for i in range(j):
            list.append(queue.remove_max()[1])
        return list
