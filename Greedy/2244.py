class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        def genCount():
            countTasks={}
            for i in tasks:
                countTasks[i]=countTasks.get(i,0)+1
            return countTasks
        
        def solve():
            countTasks=genCount()
            ans=0
            for key,value in countTasks.items():
                if(value==1):
                    return -1
                else:
                    if(value>=3):
                        if(value%3==1):
                            ans+=((value-4)//3)+2            
                        elif(value%3==2):
                            ans+=(value//3)+1
                        else:
                            ans+=value//3
                    else:
                        ans+=1
            return ans
        return solve()
        

# TC o(n) S O(n)

