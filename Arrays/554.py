class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countDic={}
        preSumCollect={}
        preSumArray=[]
        layerCount=0
        for layer in wall:
            if(len(layer)==1):
                layerCount+=1
        if(layerCount==len(wall)):
            return layerCount
        for layer in wall:
            preSum=0
            preSumArraySet=set()
            for i in layer:
                preSum=preSum+i
                preSumCollect[preSum]=preSumCollect.get(preSum,0)+1
                preSumArraySet.add(preSum)
            preSumArray.append(preSumArraySet)
            preSumCollect[preSum]=0
        maxKey=None
        maxValue=float("-inf")
        for key,value in preSumCollect.items():
            if(value>maxValue):
                maxKey=key
                maxValue=value
        ans=0
        for i in preSumArray:
            if(maxKey not in i):
                ans+=1
        return ans

        # Time Complexity O(n^2)
