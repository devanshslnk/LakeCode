class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> 
int:
        def getDiffArr():
            pnc=[(profits[i],capital[i]) for i in range(len(capital))]
            pnc=sorted(pnc,key=lambda x:x[1])
            return pnc
        def getIndex(pnc,w):
            for i in range(len(pnc)):
                if(pnc[i][1]>w):
                    return i-1
            return len(pnc)-1 
        def updateHeap(heap,pnc,index,prevIndex):
            for i in range(prevIndex,index+1):
                heapq.heappush(heap,(-pnc[i][0],pnc[i]))  
        def solve(k,w):
            count=0
            heap=[]
            pnc=getDiffArr()
          
            prevIndex=0
            index=getIndex(pnc,w)
         
            updateHeap(heap,pnc,index,prevIndex)
            while(count<k and heap):
          
                diff,pair=heapq.heappop(heap)
                w+=pair[0]
                count+=1
                if(index<len(pnc)-1):
                    prevIndex=index+1

                    index=getIndex(pnc,w)        
                    updateHeap(heap,pnc,index,prevIndex)
            return w
        return solve(k,w)

# Tc nlogn Sc o(n)



