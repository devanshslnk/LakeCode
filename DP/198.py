class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve():
            dp=[0]*len(nums)
            ans=float("-inf")
            for i in range(len(nums)):
                if(i==0):
                    dp[i]=nums[i]
                elif(i==1):
                    dp[i]=nums[i]
                else:
                    for j in range(i-2,-1,-1):
                        dp[i]=max(dp[i],dp[j]+nums[i])
                ans=max(ans,dp[i])
            return ans
        return solve()
    # TC O(n^2) SC O(n)
