class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        def solve():
            sTrips=sorted(trips,key=lambda x:x[1])
            heap=[]
            currC=0
            print(sTrips)
            for i in range(len(sTrips)):
                 
                while(heap and heap[0][0]<=sTrips[i][1]):
                    dest,start,cp=heapq.heappop(heap)
                    currC-=cp
                if(capacity-currC>=sTrips[i][0]):
                    heapq.heappush(heap,(sTrips[i][2],sTrips[i][1],sTrips[i][0]))
                    currC+=sTrips[i][0]
                else:

                    return False


            return True


        return solve()

# TC O(nlogn) SC O(n)
