class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        def createTimerHeap():
            timerHeap=[]
            for idx,val in enumerate(tasks):
                heapq.heappush(timerHeap,(val[0],val[1],idx))
            return timerHeap


        def getTasks(timer,timerHeap,heap):
    
            while(timerHeap):
                if(timerHeap[0][0]<=timer):
                    eTime,pTime,idx=heapq.heappop(timerHeap)
                    heapq.heappush(heap,(pTime,idx))
                else:
                    break
        def solve():
            timerHeap=createTimerHeap()
            timer=timerHeap[0][0]
            doneCount=0
            ans=[]
            heap=[]
            while(doneCount<len(tasks)):
                getTasks(timer,timerHeap,heap)
                if(heap):
                    pTime,idx=heapq.heappop(heap)
                    ans.append(idx)
                    doneCount+=1
                    timer+=pTime
                else:
                    timer=timerHeap[0][0]
            return ans      


        return solve()

# TC O(nlogn) SC O(n)
