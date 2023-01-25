class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def createHeap():
            heap=[]
            for i in costs:
                heapq.heappush(heap,(-abs(i[0]-i[1]),i))
            return heap
        def solve():
            heap=createHeap()
            firstCount=secondCount=ans=0
            n=len(costs)//2
            while(heap):
                value,i=heapq.heappop(heap)
                if(firstCount<n and secondCount<n):
                    if(i[0]<=i[1]):
                        ans+=i[0]
                        firstCount+=1
                    else:
                        ans+=i[1]
                        secondCount+=1
                elif(firstCount==n):
                    ans+=i[1]
                    secondCount+=1
                elif(secondCount==n):
                    ans+=i[0]
                    firstCount+=1
            return ans
            
        return solve()

# Time Complexity O(nlogn) Space Complexity O(n)
        

