class Solution:
    def countAndSay(self, n: int) -> str:
        # so basically its a sequnce whose working pattern is 
        # base cae is if n = 1 we return 1
        # if n=2 means  upar x ka count and what is the x? = one time  ,one= 11
        # if n= 3 then count of x = 2 and x is 1=21
        # if n = 4 then count of previous  = 1211 one time 2 and one time 1 above
        # if n = 5 count = one time 1 one time 2 two time 1 = 111221
        def solve(n, currElm):
            # Base case
            if n == 1:
                return "1"
            elem = solve(n - 1, currElm )
            # If only one character
            if len(elem) == 1:
                return "1" + elem
            # one for case having len above then 1==11 or more than  that
            final = []
            prefix = "1"
            prev = elem[0]
            for i in range(1, len(elem)):
                curr = elem[i]
                if curr == prev:
                    # increase count
                    prefix = str(int(prefix)+1)
                else:
                    final.append(prefix + prev) 
                    prefix = "1"                 
                    prev = curr           
                # last grp
            final.append(prefix + prev) 
            return "".join(final)

        currElm = ""
        final = []
        ans = solve(n, currElm)
        return ans