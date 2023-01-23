class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    
#     calculate the entire each row
        def calcRow(rowNumber,prevArray):
            newArray=prevArray[:]
            for i in range(1,rowNumber):     
                newArray[i]=prevArray[i-1]+prevArray[i]
            newArray.append(1)
            return newArray

#          calculates the entire triangle
        def calcTriangle(rowNumber,ans):
#           base condition
            if(rowNumber==0):
                ans.append([1])
                return [1]
            prevArray=calcTriangle(rowNumber-1,ans)
            newArray=calcRow(rowNumber, prevArray[:])
            ans.append(newArray)
            return newArray
  
        ans=[]
        finalArray=calcTriangle(numRows-1,ans)
        return ans
# Complexty O(n^2)
        
