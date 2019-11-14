class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        num = 0
        res = 0
        st = []
        for i in range(len(s)):
            if s[i]!=" ":
                if s[i].isdigit():
                    num = num*10 + int(s[i])
                if s[i] in ["-","+"]:
                    res += sign*num
                    num,sign = 0,[1,-1][s[i]=="-"]
                if s[i] == "(":
                    st.append(res)
                    st.append(sign)
                    res,sign = 0,1
                if s[i] == ")":
                    res += sign*num
                    res *= st.pop()
                    res += st.pop()
                    num = 0
        return res + sign*num
                    