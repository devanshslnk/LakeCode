class Solution:
    def integerBreak(self, n: int) -> int:
        def solve(currProd,num):
            if(num==0):
                
                return currProd
            if(num<0):
                return 0
            if(dp.get((currProd,num))!=None):
                return dp[(currProd,num)]
            i=1
            temp=0
            while(i<=num and i!=n):
                temp=max(temp,solve(currProd*i,num-i))
                i+=1
            dp[(currProd,num)]=temp
            return temp

        dp={}
        return solve(1,n)


        
