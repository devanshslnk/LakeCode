class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def solve(curr,ans,currSum):
            if(currSum==target):
                ans.add(tuple(sorted(curr[:])))
            if(currSum>target):
                return 

            for i in range(len(candidates)):
                curr.append(candidates[i])
                solve(curr,ans,currSum+candidates[i])
                curr.pop()
            


        ans=set()
        solve([],ans,0)
        return list(ans)
# TC O(n^n) SC O(n)


