class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array=s.split(" ")
        final=[]
        print(array)
        for i in range(len(array)):
            if(len(array[i])==0):
                continue
            else:
                final.append(array[i])
        
        return len(final[-1]
