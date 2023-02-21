class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        def solve(start,currSum):
            if(currSum==amount):
                return 1
            if(currSum>amount):
                return 0
            if(start>=len(coins)):
                return 0
            if(dp.get((start,currSum))!=None):
                return dp[(start,currSum)]
            temp=0
            for i in range(start,len(coins)):
                temp+=solve(i,currSum+coins[i])
            dp[(start,currSum)]=temp
            return temp
        return solve(0,0)

# TC O(N*Amoount) SC TC (N*Amount)
            
