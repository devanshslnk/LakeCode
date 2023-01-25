class Solution:
    def minSwaps(self, s: str) -> int:
        stack=[]
        for i in s:
            if(not stack):
                stack.append(i)
            else:
                if(i=="]" and stack[-1]=="["):
                    stack.pop()
                    continue
                stack.append(i)
        
        return math.ceil((len(stack))/4)

# Time complexity O(n) space complextiy O(n)
