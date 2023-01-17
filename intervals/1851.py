class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        def solve():
            queryIndex={value:[] for index,value in enumerate(queries)}
            for index,value in enumerate(queries):
                queryIndex[value].append(index)
            queryKeys=list(queryIndex.keys())
            queryKeys.sort()
            ans={}
            intervals.sort()
            hmap={}
            heap=[]
            i=0
            for query in queryKeys:
                while(i<len(intervals) and intervals[i][0]<=query ):
                    heapq.heappush(heap,(intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                    i+=1
                while(heap and heap[0][1]<query):
                    heapq.heappop(heap)
            
                ans[query]=heap[0][0] if heap else -1

            finalAns=[-1]*len(queries)
            for key,value in ans.items():
                for i in queryIndex[key]:
                    finalAns[i]=value

            return finalAns
        return solve()
    # Timecomlexity n^2logn


