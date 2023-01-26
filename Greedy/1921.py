class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        def createTimesHeap():
            times=[]
            for idx,val in enumerate(dist):
                # times.append(val/speed[idx])
                heapq.heappush(times,val/speed[idx])
            return times

        def solve():
            times=createTimesHeap()
            timer=0
            counter=0
            while(times):
                time=heapq.heappop(times)
                if(time<=timer):
                    return timer
                else:

                    timer+=1
            return timer
        return solve()

# Time Complexity O(nlogn) SPace complexity O(n)

            

