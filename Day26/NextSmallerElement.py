class Solution:
	def nextSmallerEle(self, arr):
		# code here
# 		arr is [4,8,5,2,2,1]
		stack = [] 
		n = len(arr)
		ans = [-1 for _ in range(n)]
		for i in range(n-1,-1,-1):
		    curr = arr[i] #curr is 1
		    if len(stack) == 0 :#means empty store -1 in place of taht
		        ans[i]= -1
		        stack.append(curr) #as curr. will be someome elses nse so store it
		        continue 
		    else: #means stack has some val in it 
		  #  now check if teh top and curr like curr > top #nse found else not
		      #  top = stack[-1]
		        if curr > stack[-1] : #2>1 yes so nse is 1 measn top
		            ans[i] =stack[-1]
		            stack.append(curr) #store 2 now 
		            continue
		        else:# curr < top like 2< 5 so lets conside stack has [5,1 ]in it top is 5 for now
#now popping 5 wil have us with ans as 1
		            while len(stack)!=0 and  curr <= stack[-1] : #ya to stack khali hojaaye ya nse condition meey hojaauye
                        stack.pop() #5 popped now stack has 1 in and curr> top hogya
                    if len(stack)==0:
                        ans[i] = -1
                        stack.append(curr)
                    else:
                        if curr > stack[-1] : #2>1 yes so nse is 1 measn top
        		            ans[i] =stack[-1]
        		            stack.append(curr) #store 2 now 
        return ans