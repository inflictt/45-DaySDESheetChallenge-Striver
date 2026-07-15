class Solution:
    def search(self, pat, txt):
        def buildLPS(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0
            i = 1

            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = buildLPS(pat)

        ans = []
        i, j = 0, 0

        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1

            if j == len(pat):
                ans.append(i - j)      # instead of return
                j = lps[j - 1]         # continue searching

            elif i < len(txt) and txt[i] != pat[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return ans