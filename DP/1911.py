class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp={}
        def solve(i,select):
            if(i>=len(nums)):
                return 0
            temp=float("-inf")
            if(dp.get((i,select))!=None):
                return dp[(i,select)]
            if(select):
                selected=solve(i+1,not select)+nums[i]
                notSelected=solve(i+1,select)
                temp=max(selected,notSelected)
            else:
                selected=solve(i+1,not select)-nums[i]
                notSelected=solve(i+1,select)
                temp=max(selected,notSelected)
            dp[(i,select)]=temp
            return temp

        return solve(0,True)

# TC O(n) SC O(n)





                

