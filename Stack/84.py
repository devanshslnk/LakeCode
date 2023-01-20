class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
        def balanceStack(stack,height):
            #  do balancing here
            ogLen=len(stack)
            localArea=float("-inf")
            counter=len(stack)-1
            while(counter>=0 and stack[counter]>height):
                tempHeight=stack[counter]
                stack[counter]=height
                localArea=max(localArea,tempHeight*(ogLen-counter))
                counter-=1
            return localArea

        def solve():
            stack=[heights[0]]
            area=heights[0]
            for i in range(1,len(heights)):
                if(heights[i]<stack[-1]):
                    maxArea=balanceStack(stack,heights[i])
                    area=max(area,maxArea)
                    stack.append(heights[i])
                else:
                    stack.append(heights[i])
            area=max(area,balanceStack(stack,float("-inf")))

            return area

        return solve()

        # Time Complexity O(N) Space Complextiy O(N)
