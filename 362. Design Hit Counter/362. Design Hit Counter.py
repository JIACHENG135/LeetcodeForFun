from bisect import bisect_right

class HitCounter(object):

    def __init__(self):
        self.coll = []

    def hit(self, timestamp):
        self.coll.append(timestamp)
        

    def getHits(self, timestamp):
        lo = bisect_right(self.coll, timestamp-300)
        
        ## safely can remove old elems, since new query will have greater timestamp
        self.coll = self.coll[lo:]
        
        return len(self.coll)