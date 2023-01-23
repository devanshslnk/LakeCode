class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left,right=0,0
        count=0
        while(right<len(nums)):
            if(nums[right]==val):
                right+=1
                count+=1
                continue
            nums[left]=nums[right]
    
            left+=1
            right+=1
        
        return len(nums)-count

        # Time Complexity O(n) Space Complexti O(1)
        
