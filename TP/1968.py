class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def swap(nums):
            left,right=0,2
            while(right<len(nums)):
                mid=left+(right-left)//2
                if((nums[left]+nums[right])/2==nums[mid]):
                    nums[mid],nums[left]=nums[left],nums[mid]
                left+=1
                right+=1
        def check(nums):
            left,right=0,2
            while(right<len(nums)):
                mid=left+(right-left)//2
                if((nums[left]+nums[right])/2==nums[mid]):
                    return True
                left+=1
                right+=1
            return False

        def solve():
            nums.sort()
            while(True):
                if(check(nums)):
                    swap(nums)
                else:
                    break
            return nums


                
            return nums


        return solve()
