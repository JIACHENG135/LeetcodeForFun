def findAvailableTime(meetings,schedules):
    # [0,1,2] -> [sch1,sch2,sch3]
    def helper(intv1,intv2):
        ans = []
        toList = lambda x:[list(i) for i in x]
        intv1 = toList(intv1)
        intv2 = toList(intv2)
        intv1.sort()
        intv2.sort()
        a,b = len(intv1),len(intv2)
        i,j = 0,0
        while i<a and j<b:
            if intv1[i][1]<intv2[j][1]:
                cur = intv1[i]
                i += 1
            else:
                cur = intv2[j]
                j += 1
            if not ans:
                ans.append(cur)
            else:
                ma,mi = max(cur[0],ans[-1][0]),min(cur[1],ans[-1][1])
                if ma<=mi:
                    ans[-1][1] = max(cur[1],ans[-1][1])
                else:
                    ans.append(cur)
        if i<a:
            ans.extend(intv1[i:])
        else:
            ans.extend(intv2[j:])
        return ans
    def divide(intervals):
        # print(intervals,len(intervals))
        if len(intervals) == 1:
            return intervals
        else:
            while len(intervals)>1:
                res = []
                l = len(intervals)
                for i in range(l//2):
                    res.append(helper(intervals[2*i],intervals[2*i+1]))
                if l%2:
                    res.append(intervals[l//2])
                intervals = divide(res)
            return intervals
    
    res = []
    for p in schedules:
        res.append(meetings[p])
    res = divide(res)
    origin = 0
    ans = []
    print(res[0])
    res = res[0]
    for start,end in res:
        ans.append([origin,start])
        origin = end
    if origin<2400:
        ans.append([origin,2400])
    return ans
            











meeting =  [[(1230, 1300),( 845, 900),(1300, 1500)],[( 930, 1200),(1515, 1546),(1600, 2359)],[( 845, 915),(1515, 1545),(1235, 1245)]]

schedule = [0,1,2]

a = findAvailableTime(meeting,schedule)
print(a)