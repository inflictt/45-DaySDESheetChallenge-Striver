class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = ""
        for i in range(len(s)):
            ch = s[i]
            if ch == " ":  # this is a space means a word is completed now
                if word:
                    stack.append(word)
                    word = ""

            else:  # letter coming so add to word
                word += ch
        if word: #checks for the last words appending 
            stack.append(word)
        stack.reverse()
        return " ".join(stack)
