class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def solve():
            dp=[[[0,0] for i in range(len(piles))]for j in range(len(piles))]
            offset=1
            for i in range(len(piles)):
                dp[i][i]=[piles[i],0]
            for i in range(1,len(piles)):
                row=0
                col=i
                while(row<len(piles) and col<len(piles)):
                    if(piles[col]+dp[row][col-1][1]>piles[row]+dp[row+1][col][1]):
                        dp[row][col][0]=piles[col]+dp[row][col-1][1]
                        dp[row][col][1]=dp[row][col-1][0]
                    else:
                        dp[row][col][0]=piles[row]+dp[row+1][col][1]
                        dp[row][col][1]=dp[row+1][col][0]
                    col+=1
                    row+=1

            return dp[0][-1][0]>dp[0][-1][1]
        return solve()
# TC O(n^2) SC O(n*2)
                        

