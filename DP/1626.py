class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        def getSortedHmap():
            hmap={}
            for i in range(len(scores)):
                hmap[i]=(scores[i],ages[i])
            
            return sorted(hmap.items(),key= lambda x:(x[1][1],x[1][0]))

        def solve():
            dp=[0]*len(scores)
            hmap=getSortedHmap()
            for i in range(len(scores)-1,-1,-1):
                dp[i]=hmap[i][1][0]
                for j in range(i+1,len(scores)):
                    if(hmap[i][1][0]<=hmap[j][1][0]):
                        dp[i]=max(dp[i],hmap[i][1][0]+dp[j])

            return max(dp)
        return solve()

# TC O(n^2) SC O(n)

