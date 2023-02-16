class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        def solve(s,start,wordSet,dic,dp):
            
            if(start==len(s)):
                return True
            
            flag=False
            for i in range(start,len(s)):
                
                if(dic[(start,i)] in wordSet):
                    if(dp.get(i+1)!=None):
                        flag+=dp[i+1]
                    else:
                        
                        flag+=solve(s,i+1,wordSet,dic,dp)
                        dp[i+1]=flag
                     
                if(flag):
                    return True
                    
            return flag
            
        wordSet=set(wordDict)
        dic={}
        dp={}
        for i in range(len(s)):
            for j in range(i,len(s)):
                dic[(i,j)]=s[i:j+1]

        return solve(s,0,wordSet,dic,dp)

#  TC O(n^3) SC O(N)
