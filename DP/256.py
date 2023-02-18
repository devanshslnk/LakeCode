class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def solve():
            dp=[[float("+inf") for i in range(3)] for j in range(len(costs))]
            for i in range(3):
                dp[0][i]=costs[0][i]
            print(dp)
            for i in range(1,len(costs)):
                for j in range(3):
                    
                    for k in range(3):
                        if(j!=k):
                            dp[i][j]=min(dp[i][j],dp[i-1][k])
                    dp[i][j]+=costs[i][j]

            return min(dp[-1][:])

        return solve()
