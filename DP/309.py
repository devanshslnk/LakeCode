class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def  calc(i,buying):
            if(i>=len(prices)):
                return 0
            temp=float("-inf")
            if(dp.get((i,buying))!=None):
                return dp[(i,buying)]
            if(buying):
                buy=calc(i+1,not buying)-prices[i]
                cool=calc(i+1,buying)
                temp=max(buy,cool)
            else:
                sell=calc(i+2,not buying)+prices[i]
                cool=calc(i+1,buying)
                temp=max(sell,cool)

            dp[(i,buying)]=temp
            return temp

        return calc(0,True)

# TC O(n) SC O(n)



         
