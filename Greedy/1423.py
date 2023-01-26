class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        def createPresum():
            preSum=[]
            curr=0
            preSum.append(curr)
            for i in cardPoints:
                curr+=i
                preSum.append(curr)
            return preSum 
        def solve():
            preSum=createPresum()
            totalPoints=preSum[-1]
            left,right=1,len(cardPoints)-k 
            if(k==len(cardPoints)):
                return totalPoints
            ans=0
            while(right<len(preSum)):
                tempSum=preSum[right]-preSum[left-1]
                ans=max(ans,totalPoints-tempSum)
                left+=1
                right+=1
            return ans 
        return solve()

# Time complexity O(n) Space Complexity O(n)
                

