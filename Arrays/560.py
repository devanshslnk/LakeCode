class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq=defaultdict(lambda:0)
        presum=[0]*len(nums)
        presum[0]=nums[0]
        ans=0
        freq[nums[0]]=1
        if(nums[0]==k):
            ans+=1
        for i in range(1,len(nums)):
            presum[i]=presum[i-1]+nums[i]
            
            
            if(presum[i]==k):
                ans+=1

            if(freq[presum[i]-k]!=0):

                ans+=freq[presum[i]-k]

            freq[presum[i]]+=1
                    

        
        # print(ans)
        return ans
    # Time Complexity O(n^2) Space Complexity O(2*n)
