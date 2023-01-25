class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        uniqueCharMap={}
        ans=0
        letterSet=set()            
        for index,value in enumerate(s):
            if(uniqueCharMap.get(value)==None):
                uniqueCharMap[value]=[index,None]
            else:
                uniqueCharMap[value][1]=index
        result=set([])
        for key,value in uniqueCharMap.items():
            if(value[1]!=None):
                for i in range(value[0]+1,value[1]):
                    result.add(key+s[i]+key)

        return len(result)

# Time Complexity O(26*n) space complextiy O(26+nC3)



