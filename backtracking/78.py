class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(curr,ans,start):
            if(start>len(nums)):
                return 
            
            ans.append(curr[:])
            for i in range(start,len(nums)):
                curr.append(nums[i])
                solve(curr,ans,i+1)
                curr.pop()
            

        

        ans=[]
        solve([],ans,0)
        return ans 

# TC O(n*2^n) SC O(n)
