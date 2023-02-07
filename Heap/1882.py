class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        def createHeap():
            serverHeap=[]
            for idx,val in enumerate(servers):
                heapq.heappush(serverHeap,(val,idx))
            return serverHeap
        def solve():
            serverHeap=createHeap()
            busyServer=[]
            ans=[]
            for i in range(len(tasks)):
                
                while(busyServer and busyServer[0][0]<=i):
                    time,val,idx=heapq.heappop(busyServer)
                    heapq.heappush(serverHeap,(val,idx))
                if(serverHeap):
                    val,idx=heapq.heappop(serverHeap)
                    ans.append(idx)
                    heapq.heappush(busyServer,(i+tasks[i],val,idx))
                else:
                    time,val,idx=heapq.heappop(busyServer)
                    ans.append(idx)
                    heapq.heappush(busyServer,(time+tasks[i],val,idx))
            
            return ans

        return solve()
        

# TC O(nlogn) SC O(n)
