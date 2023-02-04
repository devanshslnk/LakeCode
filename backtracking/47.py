class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def solve(curr,visited,ans):
            if(len(curr)==len(nums)):
                ans.add(tuple(curr[:]))
            if(len(curr)>len(nums)):
                return 
            for i  in range(len(nums)):
                if(visited[i]==1):
                    continue
                visited[i]=1
                curr.append(nums[i])
                solve(curr,visited,ans)
                visited[i]=0
                curr.pop()

        visited=[0]*len(nums)
        ans=set()
        solve([],visited,ans)
        return list(ans)
