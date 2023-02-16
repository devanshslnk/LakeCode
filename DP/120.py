class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # def solve(i,index,currSum):
        #     if(i==len(triangle)):
        #         return currSum

        #     temp=min(solve(i+1,index,triangle[i][index]+currSum),solve(i+1,index+1,triangle[i][index+1]+currSum))
        
        #     return temp
                
        
        # return solve(1,0,triangle[0][0])
        def solve():

            dp=[[0 for i in range(len(triangle))] for j in range(len(triangle))]
            for i in range(len(triangle[-1])):
                dp[-1][i]=triangle[-1][i]
            for i in range(len(triangle)-2,-1,-1):
                for j in range(i,-1,-1):
                    dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]

            return dp[0][0]

        return solve()

# TC O(n^2) SC O(N^2)
