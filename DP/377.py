class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def solve(currSum,dp):
            if(currSum==target):
                return 1
            if(currSum>target):
                return 0
            if(dp.get(currSum)!=None):
                return dp[currSum]
            temp=0
            for i in range(len(nums)):
                temp+=solve(currSum+nums[i],dp)
            dp[currSum]=temp
            return temp
        dp={}
        return solve(0,dp)

# TC O(target*n) SC O(n)
