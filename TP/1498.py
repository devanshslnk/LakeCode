class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        def binarySearch(idx,nums):
            left,right=idx,len(nums)-2
            
            while(left<=right):
                mid=left+(right-left)//2
                
                if(nums[idx]+nums[mid]<=target):
                    if(nums[idx]+nums[mid-1]<=target and nums[idx]+nums[mid+1]<=target):
                        left=mid+1
                    elif(nums[idx]+nums[mid-1]<=target and nums[idx]+nums[mid+1]>target):
                        return mid
                else:
                    right=mid-1

            return -1

        def solve():
            nums.sort()
            nums.append(float("+inf"))
            nums.insert(0,float("-inf"))
            ans=0
        
            for i in range(1,len(nums)-1):
                if(nums[i]>=target):
                    break
                binTest=binarySearch(i,nums)
                print(i,binTest)
                if(binTest==-1):
                    break
                else:
                    diffPow=binTest-i
                    ans+=(2**diffPow)-1
                    if(nums[i]*2<=target):
                        ans+=1
            return ans%((10**9)+7)
        return solve()

# TC O(nlogn) SC = O(1)
