
# 第⼀题:

# 给⼀个string，把⾥⾯的⼩写字⺟转成⼤写字⺟，类似于

# combination： abC -> AbC, aBC, abC, ABC. ⽤了backtrace，跑了⼀下没啥

# 问题。


def gen_upper_case(s):
    res = set()
    arr = [0] * len(s) # [0,0,0]
    
    helper(res, len(s), arr, 0, s)
    return res

def helper(res, n, arr, i, s):
    if i == n:
        print(arr)
        tmp = ''
        for j in range(len(arr)):
            if arr[j]:
                tmp += s[j].upper()
            else:
                tmp += s[j]
        res.add(tmp)
        return
    
    arr[i] = 0
    helper(res, n, arr, i+1, s)

    arr[i] = 1
    helper(res, n, arr, i+1, s)


print(gen_upper_case('abC'))