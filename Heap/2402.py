class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        def solve(n,meetings):
            meetings=sorted(meetings,key=lambda x:x[0])
            ans={i:0 for i in range(n)}
            heap1=[i for i in range(n)]
            heap2=[]
            heapq.heapify(heap1)
            for i in range(len(meetings)):
                while(heap2 and heap2[0][0]<=meetings[i][0]):
                    tempEnd,tempRoom=heapq.heappop(heap2)
                    heapq.heappush(heap1,tempRoom)             
                if(heap1):
                    room=heapq.heappop(heap1)
                    ans[room]+=1
                    heapq.heappush(heap2,(meetings[i][1],room))
                else:
                    end,room=heapq.heappop(heap2)
                    ans[room]+=1
                    heapq.heappush(heap2,(end+(meetings[i][1]-meetings[i][0]),room))
            finalAns=float("+inf")
            maxi=float("-inf")
            for key,value in ans.items():
                if(value>maxi):
                    finalAns=key
                    maxi=value
                elif(value==maxi):
                    finalAns=min(finalAns,key)
            return finalAns    
        return solve(n,meetings)
# TC nlogn SC N


