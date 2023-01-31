class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findTwoSum(nums,i,j):
            localTarget=target-nums[i]-nums[j]
            left,right=0,len(nums)-1
            pairs=[]
            while(left<right):
                if(right==i or right==j):
                    right-=1
                    continue
                if(left==i or left==j):
                    left+=1
                    continue
                # if(left==i or left==j):
                #     left+=1
                #     if(right==i or right==j):
                #        right-=1
                #     continue
                if(left<right):
                    temp=nums[left]+nums[right]
                    if(temp==localTarget):
                        pairs.append((left,right))
                        left+=1
                        right-=1
                    elif(temp>localTarget):
                        right-=1
                    else:
                        left+=1

                else:
                    break

            return pairs
        
        def solve():
            nums.sort()
            ansSet=set()
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    pairs=findTwoSum(nums,i,j)
                    for pair in pairs:
                        temp=[nums[pair[0]],nums[pair[1]],nums[i],nums[j]]
                        temp.sort()
                        ansSet.add(tuple(temp))
            return ansSet

        return solve()


# TC O(n^3) SC O(n)
