class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def identifySet(curr,a,b):
            tempSet=set([])
            for idx,i in enumerate(triplets):
                if(i[curr]==target[curr] and i[a]<=target[a] and i[b]<=target[b]):
                    tempSet.add(idx)
            return tempSet

        def solve():
            setA=identifySet(0,1,2)
            setB=identifySet(1,0,2)
            setC=identifySet(2,0,1)   
            return setA and setB and setC


        return solve()

        # Time Complexity O(n) space complexity O(3*n)
        # https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/
