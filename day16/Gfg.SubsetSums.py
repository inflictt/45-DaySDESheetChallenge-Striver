class Solution:
	def subsetSums(self, arr):
		# code here
		def solve(arr,total, i , final):

		    if i == len(arr):
		        final.append(total)
		        return 
		    
		  #  pick 
            pick =  solve(arr,total+arr[i], i+1 , final)
            notPick =  solve(arr,total, i+1 , final)
		  #not pick
		final = []
        solve(arr,0 , 0 , final)
		return final





    