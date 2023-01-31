class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        delted=False
        while(left<=right):
            if(s[left]==s[right]):
                left+=1
                right-=1
            else:
                break
        if(left>right):
            return True
        templeft,tempright=left,right
        tempright-=1

        while(templeft<=tempright):
            if(s[templeft]==s[tempright]):
                templeft+=1
                tempright-=1
            else:
                break

        if(templeft>tempright):
            return True
        templeft,tempright=left,right
        templeft+=1
        while(templeft<=tempright):
            if(s[templeft]==s[tempright]):
                templeft+=1
                tempright-=1
            else:
                return False 



        return True

# Time complexity O(n) Space complexity O(1)
