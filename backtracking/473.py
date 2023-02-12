class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k=4
        nums=matchsticks[:]
        def solve(start,k,used,currSum,target):
            if(k==0):
                return True
            if(currSum==target):
                return solve(0,k-1,used,0,target)

            for i in range(start,len(nums)):
                if i > 0 and used[i-1]==False and nums[i] == nums[i - 1]:
                    continue
                if(used[i]==False and currSum+nums[i]<=target):
                    used[i]=True
                    if solve(i+1,k,used,currSum+nums[i],target):
                        return True
                    used[i]=False
                
            return False

    
        used=[False]*len(nums)
        
        target=sum(nums)//k
        if(sum(nums)%k!=0):
            return False
        nums.sort(reverse=True)
        return solve(0,k,used,0,target)

# TC O(2^n) SC O(n)
