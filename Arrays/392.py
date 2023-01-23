class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sCounter=0
        for i in t:
            if(sCounter<len(s) and i==s[sCounter]):
                sCounter+=1
                
        return sCounter==len(s)
