class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def solve():
            dp=[0]*(len(cost)+1)
            cost.append(0)
            for i in range(len(cost)):
                if(i==0):
                    dp[0]=cost[0]
                elif(i==1):
                    dp[1]=cost[1]
                else:
                    dp[i]=min(dp[i-1],dp[i-2])+cost[i]
            return dp[-1]
        return solve()

    # TC O(n) SC O(n)
