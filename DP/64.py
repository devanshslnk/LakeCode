class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def solve():
            # Lets Solve this
            dp=[[0 for i in range(len(grid[0]))] for j in range(len(grid))
            ]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if(i==0 and j==0):
                        dp[i][j]=grid[i][j]
                    elif(i==0):
                        dp[i][j]=grid[i][j]+dp[i][j-1]
                    elif(j==0):
                        dp[i][j]=grid[i][j]+dp[i-1][j]
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
            print(dp)
            return dp[-1][-1]
        return solve()
# TC O(n^2) SC O(N^2)

