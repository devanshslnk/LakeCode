class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def solve():
            sPoints=sorted(points,key=lambda x:x[0])
            idx=0
            ans=0
            # print(sPoints)
            while(idx<len(sPoints)):
                left,right=sPoints[idx]
                idx+=1
                while(idx<len(sPoints) and sPoints[idx][0]<=right):
                    right=min(sPoints[idx][1],right)
                    idx+=1
                ans+=1
            return ans
        return solve()
# Tc O(nlogn) SC O(n)


