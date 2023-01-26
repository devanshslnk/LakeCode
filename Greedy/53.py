class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pointer=currSum=0
        maxSum=float("-inf")
        n=len(nums)
        while(pointer<n):
            currSum+=nums[pointer]
            if(currSum<nums[pointer]):
                currSum=nums[pointer]
            maxSum=max(maxSum,currSum)
            pointer+=1
        return maxSum


# Time complexity O(n) space complexity O(1)
