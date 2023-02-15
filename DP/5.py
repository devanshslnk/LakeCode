class Solution:
    def longestPalindrome(self, s: str) -> str:
        def solve():
            dp=[[False for i in range(len(s))] for j in range(len(s))]
            maxLen=0
            ans=""
            for i in range(len(s)):
                dp[i][i]=True
                maxlen=1
                ans=s[i]
            
            for i in range(len(s)-1,-1,-1):
                for j in range(i+1,len(s)):
                    if(s[i]==s[j]):
                        if(j==i+1 or dp[i+1][j-1]==True):
                            dp[i][j]=True
                            if(j-i+1>maxLen):
                                maxLen=j-i+1
                                ans=s[i:j+1]
            return ans
        return solve()

# TC O(n^2) SC O(N^2)
