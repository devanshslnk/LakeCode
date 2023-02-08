class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def solve():
            bCount=0
            bmap={"b":0,"a":0,"l":0,"o":0,"n":0}
            ans=0
            for i in range(len(text)):
                if(bmap.get(text[i])!=None):
                    bmap[text[i]]+=1
            count=min(bmap["b"],bmap["a"],bmap["n"],bmap["l"]//2,bmap["o"]//2)
            return count                
                
            
                


        return solve()

    # TC O(n) SC O(1)
