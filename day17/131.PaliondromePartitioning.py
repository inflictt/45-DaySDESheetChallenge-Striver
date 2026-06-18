class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def checkPal(string):
            # checks if the function is palindrom string or not 
            rev = string[::-1]
            return rev==string

        def solve(idx ,string , temp , output):
            if len(string)==idx:
                output.append(temp[:])
                return

            for j in range(idx, len(s)):
                substring = s[idx:j+1]
                cp = checkPal(substring)
    
                if cp:
                    temp.append(substring)
                    solve(j+1 ,string , temp , output)
                    temp.pop()
                    
        output = []
        solve(0 ,s , [] , output)
        return output