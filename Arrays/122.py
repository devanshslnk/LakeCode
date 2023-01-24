class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[0]*len(prices)
        dp[0]=0
        for i in range(1,len(prices)):
            if(prices[i-1]>=prices[i]):
                dp[i]=dp[i-1]
            else:
                for j in range(i-1,-1,-1):
                    if(prices[i]>prices[j]):
                        dp[i]=max(dp[i],dp[j]+prices[i]-prices[j])
        return max(dp)

        # Time Complexity O(n^2) Space Complexity O(n)
