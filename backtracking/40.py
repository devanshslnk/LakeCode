class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start,ans,curr,currSum,uniqueKeys,uniqueCount):
            if(currSum==target):
                ans.append(curr[:])
                return 
            if(currSum>target):
                return
            for i in range(start,len(uniqueKeys)):
                key=uniqueKeys[i]
                if(uniqueCount[key]>0):
                    uniqueCount[key]-=1
                    curr.append(key)
                    backtrack(i,ans,curr,currSum+key,uniqueKeys,uniqueCount)
                    uniqueCount[key]+=1
                    curr.pop()
            


        

        def solve():
            uniqueCount={}
            for i in candidates:
                uniqueCount[i]=uniqueCount.get(i,0)+1

            uniqueKeys=list(uniqueCount)
            ans=[]
            backtrack(0,ans,[],0,uniqueKeys,uniqueCount)
            return ans


        return solve()

    # TC O(2^n) SC O(n)

