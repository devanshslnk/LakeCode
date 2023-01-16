class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        dp={}
        def dfs(l,r):
            if(l>r):
                return 0
            if(l==r):
                return nums[l-1]*nums[l]*nums[r+1]
            if(dp.get((l,r))!=None):
            
                return dp[(l,r)]
            dp[(l,r)]=0
            for i in range(l,r+1):
                temp=nums[l-1]*nums[i]*nums[r+1]
                temp+=dfs(l,i-1)+dfs(i+1,r)
                dp[(l,r)]=max(dp[(l,r)],temp)
            return dp[(l,r)]
        nums=[1]+nums+[1]

        return dfs(1,len(nums)-2)
