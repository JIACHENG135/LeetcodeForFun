class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = collections.defaultdict(str)
        self.st = collections.defaultdict(list)
    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.mem[(key,timestamp)] = value
        self.st[key].insert(bisect.bisect_left(self.st[key],timestamp),timestamp)
    def get(self, key: 'str', timestamp: 'int') -> 'str':
        ind = bisect.bisect_left(self.st[key],timestamp)
        if ind==0 and not self.st[key]:
            return ''
        elif ind == 0 and self.st[key][0]!=timestamp:
            return ''
        else:
            if ind == len(self.st[key]):
                return self.mem[(key,self.st[key][-1])]
            if self.st[key][ind]==timestamp:
                return self.mem[(key,self.st[key][ind])]
            else:
                return self.mem[(key,self.st[key][ind-1])]
