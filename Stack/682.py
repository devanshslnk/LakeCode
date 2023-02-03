class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for op in operations:
            if(op=="+"):
                temp=stack[-1]+stack[-2]
                stack.append(temp)
            elif(op=="D"):
                temp=2*stack[-1]
                stack.append(temp)
            elif(op=="C"):
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
# TC O(n) SC(n)

