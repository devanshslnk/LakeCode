class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=collections.deque([])
        starStack=collections.deque([])
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(["(",i])
            elif( s[i]=="*"):
                starStack.append(i)
            else:
                if(stack and stack[-1][0]=="("):
                    stack.pop()
                else:
                    stack.append([")",i])
        if(stack):
            for i in range(len(starStack)):
                if(not stack):
                    return True
                if(stack[0][0]==")" and starStack[i]<stack[0][1]):
                    stack.popleft()
                elif(stack[0][0]=="(" and starStack[i]>stack[0][1]):
                    stack.popleft()


        return not stack

        # Time Complexity O(n+m) Space complexity O(n+m)
