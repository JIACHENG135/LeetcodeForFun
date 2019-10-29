class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [None] * 1000000

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % 1000000
        self.map[index] = value
        return None

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % 1000000
        value = self.map[index]
        if value == None:
            return -1
        else:
            return value

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % 1000000
        self.map[index] = None