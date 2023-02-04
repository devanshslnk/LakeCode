class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        def solve():
            nums=sorted(people,reverse=True)
            stack=[]
            ans=0
            for i in range(len(nums)):
                if(limit-nums[i]==0):
                    ans+=1
                else:
                    if(stack):
                        if(stack[-1]+nums[i]<=limit):
                            stack.pop()
                            ans+=1
                        else:
                            stack.append(nums[i])
                    else:
                        stack.append(nums[i])

            ans+=len(stack)
            return ans


        return solve()

# TC  O(nlogn) SC O(n)
