
class SnapshotArray:

    def __init__(self, length: int):
        self.value = collections.defaultdict(lambda:[0])
        self.arr = collections.defaultdict(lambda:[0])
        self.snapNumber = 0

    def set(self, index: int, val: int) -> None:
        # ind = bisect.bisect_left(self.value[index],self.snapNumber)
        indexList = self.arr[index]
        if self.snapNumber == indexList[-1]:
            self.value[index][-1] = val
        else:
            self.arr[index].append(self.snapNumber)
            self.value[index].append(val)
    
    def snap(self) -> int:
        self.snapNumber += 1
        return self.snapNumber-1

    def get(self, index: int, snap_id: int) -> int:

        indexList = self.arr[index]
        valueList = self.value[index]
        # print(self.arr,self.value,index,snap_id)
        # print(valueList,index,snap_id)
        ind = bisect.bisect_left(indexList,snap_id)
        if ind>=len(valueList):
            return valueList[-1]
        elif indexList[ind] == snap_id:
            return valueList[ind]
        else:
            return valueList[ind-1]