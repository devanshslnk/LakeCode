class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def createDic():
            dic={}
            for i in nums:
                dic[i]=dic.get(i,0)+1
            return dic
        def solve():
            dic=createDic()
            keys=list(dic.keys())
            keys.sort()
            dp=[0]*len(keys)
            dp[0]=keys[0]*dic[keys[0]]
            for i in range(1,len(keys)):
                
                for j in range(i-1,-1,-1):
                    if(keys[j]==keys[i]-1):
                        continue
                    else:
                        dp[i]=max(dp[j],dp[i])
                dp[i]+=+keys[i]*dic[keys[i]]
            return max(dp)
        return solve()

# TC O(n^2) SC O(n)

