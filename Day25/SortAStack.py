class Solution:
    def sortStack(self, st):
        # code here 
        def insertChecker(stack , value):
            if not stack or stack[-1] <= value:  
                # means the value is bigger than the top, so place it directly, no issue
                stack.append(value)
                return
            else:
                # if the value is smaller, e.g. stack has 41 and value is 3,
                # then pop the top element
                temp = stack.pop()  # 41 got popped, now try placing the value
                # trying to place the value again, and if below 41 there is 39
                # and it is also bigger than the value, then it will also be popped
                insertChecker(stack , value)
                # now place back the popped elements
                stack.append(temp)  # place back 39, then 41
        
        # let's go till the bottom by popping and recursion,
        # as no looping is allowed
        stack = st
        if not stack:
            return stack
        value = stack.pop()
        self.sortStack(stack)
        # currently the top value is the last value because
        # recursion stack frames work in bottom-to-top order
        # call insert function now
        insertChecker(stack , value)
        return stack