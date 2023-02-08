class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        def solve():
            count=0
            ans=None
            for num in nums:
                if(count==0):
                    ans=num
                count+=(1 if num==ans else -1)

            return ans 
        return solve()

            
# TC O(n) SC O(1)
