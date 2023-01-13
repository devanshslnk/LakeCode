class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        def createDic():
            dic={}
            heap=[]
            for index,value in enumerate(hand):
                dic[value]=dic.get(value,0)+1
            for key,value in dic.items():
                heapq.heappush(heap,(key,value))
            return dic,heap
        def solve():
            dic,heap=createDic()
    
            while(heap):
        
               
                while(heap):
                    num,temp=heap[0]
                    if(dic[num]==0):
                        num,temp=heapq.heappop(heap)
                    else:
                        break
                count=0
                while(heap and count<groupSize):
                
                    if(dic.get(num)==None or dic[num]==0):
                        return False
                    dic[num]-=1
                    num+=1
                    count+=1
            return True
        return solve()
        #  Time Complexity O(nlogn) space complextiy O(n+m)
                






            
