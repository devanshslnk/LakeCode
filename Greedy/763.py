class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def createDic():
            dic={}
            for index,value in enumerate(s):
                if(dic.get(value)==None):
                    dic[value]=[index,index]
                else:
                    dic[value][1]=index
            return dic
        def solve():
            dic=createDic()
            ans=[]
            count=0
            low,upper=dic[s[0]]
            for i in range(0,len(s)):
                ch=s[i]
                if(dic[ch][1]<=upper):
                    count+=1
                else:
                    if(upper<i):
                        low=dic[ch][0]
                    upper=dic[ch][1]
                    count+=1
                if(upper==i):
                    ans.append(count)
                    count=0
            return ans
        return solve()
        # Time Complexity O(n) Space Complexity O(n+n)
