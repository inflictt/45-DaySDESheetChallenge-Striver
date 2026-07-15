class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            brack = s[i]
            if len(stack) == 0:
                # add something to stack which should be an openening breacket onyl not a clsoe  return False not allowed
                if brack == ")" or brack == "]" or brack == "}":
                    return False
                else:
                    stack.append(brack)

            else:  # ki ab stack is not empty
                top = stack[-1]
                if (
                    (top == "(" and brack == ")")
                    or (top == "[" and brack == "]")
                    or (top == "{" and brack == "}")
                ):
                    stack.pop()
                    # means a valid one used
                elif (
                    brack == "(" or brack == "[" or brack == "{"
                ):  # got on more opn  brack
                    stack.append(brack)
                else:
                    return False
                # means a pair came and we got poped both
            # now check if stack empy at last or not
        if len(stack) != 0:
            return False
        return True
