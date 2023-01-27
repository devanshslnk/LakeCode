class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[(float("-inf"),None) for i in range(len(nums))]
        if(len(nums)==1):
            return 0
        dp[0]=(1,nums[0])
        currMax,currMaxIndex=nums[0],0
        for i in range(1,len(nums)):
            prevMax,prevCapacity=dp[i-1]
            if(prevCapacity>=i):
                dp[i]=dp[i-1][:]
            else:
                dp[i]=[dp[currMaxIndex][0]+1,currMax]
            if(i+nums[i]>currMax):
                currMax,currMaxIndex=i+nums[i],i
            
        return dp[-1][0]

    # Time COmplexity O(n)
