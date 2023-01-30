class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q=[]
        q.append(["0000"])
        minCount=None
        first=(target[0])
        second=(target[1])
        third=(target[2])
        forth=(target[3])
        visited={}
        deadendDic={}
        for i in range(10000):
            n=None
            if(i>=0 and i<=9):
                n="000"+str(i)
            elif(i>=100 and i<=999):
                n="0"+str(i)
            elif(i>=10 and i<=99):
                n="00"+str(i)
            else:
                n=str(i)
            visited[n]=False
            if(n in deadends):
                deadendDic[n]=True
            else:
                deadendDic[n]=False
            
        
                    
                
    


        if("0000" in deadends):
            return -1
        if("0000" ==target):
            return 0
        while(len(q)!=0):
            
            first=(q[0][-1][0])
            second=(q[0][-1][1])
            third=(q[0][-1][2])
            forth=(q[0][-1][3])

            minCOunt=0
            for i in range(4):
                n=int(q[0][-1][i])
                if(i==0):

                    str1=str((n+1)%10)+ second +third+forth
                    str2=str((n-1)%10)+second+third+forth
                elif(i==1):
                    str1=first+str((n+1)%10)+third+forth
                    str2=first+str((n-1)%10)+third+forth
                elif(i==2):
                    str1=first +second+str((n+1)%10)+forth
                    str2=first+second+str((n-1)%10)+forth
                else:
                    str1=first+second+third+str((n+1)%10)
                    str2=first+second+third+str((n-1)%10)
                
                if(str1==target or str2==target or q[0][-1][i]==target):
                    
                    
                    if(minCount==None or minCount>len(q[0])+1):
                        minCount=len(q[0])
                        return minCount
                    
                
                if( visited[str1]==False and deadendDic[str1]==False):
                    
                    newArr=q[0][:]
                    newArr.append(str1)
                    q.append(newArr)
                    visited[str1]=True
                if(visited[str2]==False and deadendDic[str2]==False):
                    newArr=q[0][:]
                    newArr.append(str2)
                    q.append(newArr)
                    visited[str2]=True
            q.pop(0)
        
                    
        return -1                                    
                    
            
            
        
