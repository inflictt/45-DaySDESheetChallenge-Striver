class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        ans = 0
        rangeSet = set(range(10))
        sign = ""
        # check for all leading spaces and sign
        i = 0
        while i < n:
            if s[i] == " ":  # a gap continue
                i += 1
            else:
                break
        start = i
        if start >= n:  # reached end and only gaps were there
            return 0

        # for signed one
        if len(sign) == 0:
            if s[start] == "+":
                sign = "+"
            elif s[start] == "-":
                sign = "-"
        # check for all leading spaces and sign
        if len(sign) != 0:
            start += 1
        for x in range(start, n):
            ch = s[x]
            diff = ord(ch) - ord("0")
            if diff in rangeSet:  # 0
                ans = ans * 10 + int(ch)
            else:  # diff is not  in rangeSet
                break
        # add sign to answer and return
        stringAns = sign
        stringAns += str(ans)

        result = int(stringAns)
        # rounding check im[]
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result
