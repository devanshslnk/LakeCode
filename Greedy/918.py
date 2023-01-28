class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def createPreSum():
            # newNums=nums+nums[:-1]
            newNums=nums[:]
            currSum=0
            preSum=[]
            for i in range(len(newNums)):
                currSum+=newNums[i]
                preSum.append(currSum)
            return preSum
        def createDpArray(preSum):
            dp=[]
            maxi=float("-inf")
            for i in preSum:
                maxi=max(maxi,i)
                dp.append(maxi)
            return dp
        def checkNoCycle(n):
            ans=float("-inf")
            currSum=pointer=0    
            while(pointer<n):
                currSum+=nums[pointer]
                if(currSum<nums[pointer]):
                    currSum=nums[pointer]
                ans=max(ans,currSum)
                pointer+=1
            return ans
        def solve():
            preSum=createPreSum()
            dp=createDpArray(preSum)           
            n=len(nums)
            ans=checkNoCycle(n)
            left=1
            while(left<n):
                currSum=preSum[-1]-preSum[left-1]
                currSum+=dp[left-1]
                ans=max(ans,currSum)
                left+=1
            return ans
             
        return solve()

# Time Complexity O(n) Space Complexity O(2*n)
