class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = [[False]*len(s) for _ in range(len(s))]
        ans=len(s)
        for i in range(len(s)):
            dp[i][i]=True
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if(s[i]==s[j]):
                    if(j-1==i or dp[i+1][j-1]==True):
                        dp[i][j]=True
                        ans+=1

        # print(ans)
        return ans
    # TC O(n^2) SC O (N^2)
