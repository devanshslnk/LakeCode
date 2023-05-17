class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        def solve(additionalRocks):
            diffArr=[(capacity[i]-rocks[i]) for i in range(len(rocks))]
        
            diffArr.sort()
            count=0
            for i in range(len(diffArr)):
                if(additionalRocks==0 or additionalRocks<diffArr[i]):
                    return count
                additionalRocks-=diffArr[i]
                count+=1
            return count
        return solve(additionalRocks)


# TC O(nlogn) SC o(n)
