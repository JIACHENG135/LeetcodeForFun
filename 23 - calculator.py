def calculator3(s):
    pass #...
    """
    3.follow up： 不光有数字和operator，还有一些变量，这些变量有些可以表示为一个数值，
    需要从给定的map里去get这个变量的value。然后有的变量不能转为数字，所以结果要包含这些
    不可变成数字的单词以及其他数字部分通过计算器得到的结果。
    第一題是給你一個string例如"2+3-999"回傳計算結果int.
    第二題加上parenthesis 例如"2+((8+2)+(3-999))"一樣回傳計算結果
    第三道题是加了变量名的。。会给你一个map比如{'a':1, 'b':2, 'c':3}，假设输入为"a+b+c+1"输出要是7，如果有未定义的变量，比如"a+b+c+1+d"输出就是7+d

    """

test1 = "1+2-3+4-2-1+3"
test2 = "-1+( 2+(3-4-3)+1) - (-3 + 2)+(99)"

def calculator_basic(s):
    res = 0
    i = 0
    sign = 1
    while i < len(s):
        if s[i].isdigit():
            val = ''
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            res += sign * int(val)
            continue
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        i += 1
    return res

def calculator_basic2(s):
    res = 0
    i = 0
    sign = 1
    stack =[]
    while i < len(s):
        if s[i].isdigit():
            val = ''
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            res += sign * int(val)
            continue
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif s[i] == ')':
            res *= stack.pop()
            res += stack.pop()
        i += 1
    return res

def calculator_basic_(s):
    res = 0
    sign = 1
    i = 0
    while i < len(s):
        if s[i].isdigit():
            val = ''
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            res += int(val) * sign
            continue
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        i += 1
    return res

def calculator_basic2_(s):
    res = 0
    sign = 1
    stack = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            val = ''
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            res += int(val) * sign
            continue
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
        elif s[i] == ')':
            res *= stack.pop()
            res += stack.pop()
        i += 1
    return res

def calculator_basic3_(s, mapping):
    res = [0,'']
    sign = 1
    stack = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            val = ''
            while i < len(s) and s[i].isdigit():
                val += s[i]
                i += 1
            res[0] += int(val) * sign
            continue
        elif s[i].isalpha():
            if s[i] in mapping:
                res[0] += mapping[s[i]] * sign
            else:
                if sign == 1:
                    res[1] += '+' + s[i]
                else:
                    res[1] += '-' + s[i]
        elif s[i] == '+':
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == '(':
            stack.append(res)
            stack.append(sign)
            res = [0,'']
        elif s[i] == ')':
            res[0] *= stack.pop()
            res[0] += stack[-1][0]
            res[1] += stack[-1][1]
            stack.pop()
        i += 1
    return res


def calc(a, b, op):
    if op == '+':
        for k, v in b.items():
            a[k] = a.get(k, 0) + v
        return a
    elif op == '-':
        for k, v in b.items():
            a[k] = a.get(k, 0) - v
        return a

def calculator3(s, mapping):
    d = []
    op = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            d.append({tuple():int(s[i])})
        elif s[i].isalpha():
            if s[i] in mapping:
                d.append({tuple():mapping[s[i]]})
            else:
                d.append({tuple(s[i],): 1})
        elif s[i] == '(':
            op.append(s[i])
        elif s[i] == ')':
            while op and op[-1] != '(':
                d.append(calc(d.pop(-2), d.pop(-1), op.pop()))
            op.pop() # pop (
        elif s[i] in '+-':
            if not op:
                op.append(s[i])
            else:
                while op:
                    d.append(calc(d.pop(-2), d.pop(-1), op.pop()))
                op.append(s[i])
    
    while op:
        d.append(calc(d.pop(-2), d.pop(-1), op.pop()))
    
    res = []
    for k in sorted(d[0].keys(), key=lambda x: (-len(x), x)):
        v = d[0][k]
        if v != 0:
            if not k:
                res.append(str(v))
            else:
                res.append("{}*{}".format(v, '*'.join(k)))
    return res

                    
                    

# print(calculator_basic(test1))
# print(calculator_basic_(test1))
print(calculator_basic2(test2))
print(calculator_basic2_(test2))
print(calculator_basic3_("1+1+a+b+(1+a)+b", {'a':2}))
