class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case if n == 0:break
        def solve(x,n):
            if n == 0:
                return 1

            half = solve(x, n//2)

            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        if n <0:
            ans = solve(x , -n)
            return 1/ans
        else:
            ans = solve(x,n)
            return ans