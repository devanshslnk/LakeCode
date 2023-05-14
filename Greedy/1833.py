class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        def getCountArr(maxEle):
            countArr=[0]*(maxEle+1)
            for i in costs:
                countArr[i]+=1
            for i in range(1,len(countArr)):
                countArr[i]+=countArr[i-1]
            return countArr     

        def countSort():
            maxEle=max(costs)
            countArr=getCountArr(maxEle)
            sortedArr=[None]*len(costs)
            for i in range(len(costs)):
                sortedArr[countArr[costs[i]]-1]=costs[i]
                countArr[costs[i]]-=1
            return sortedArr



        def solve(coins):
            sortedArr=countSort()
            ans=0
            for i in sortedArr:
                coins-=i
                if(coins<0):
                    return ans
                else:
                    ans+=1
            return ans

        return solve(coins)
# TC O(n+max(costs)) SC O(max(costs))
