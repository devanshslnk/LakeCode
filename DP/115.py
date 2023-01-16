class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        def dfs(pos,start,tlen,slen):
            if(pos==tlen):
                return 1
            if(start>=slen):
                return 0
            if(dp.get((pos,start))!=None):
                return dp[(pos,start)]
            temp=0
            temp+=dfs(pos,start+1,tlen,slen)
            if(t[pos]==s[start]):
                temp+=dfs(pos+1,start+1,tlen,slen)
            dp[(pos,start)]=temp
            return temp

        return dfs(0,0,len(t),len(s))

