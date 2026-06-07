class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first to sell i need to buy 
        minPrice = prices[0]
        maxProfit = 0 
        for i in range(1,len(prices)):#this is the loop itr over prices everytime we got a price we will check it if it is minimum price to buy or not and along with we willl check if the profit is maximum or not
            price = prices[i]#currnt price eg 7
            minPrice=min(minPrice,price)#either 7 or 0 wich is 0
            maxProfit = max(maxProfit,price-minPrice)
        return maxProfit
        # Track minimum buying price  .
        # Update maximum profit while traversing  