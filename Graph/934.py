class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def checkValid(i,j):
            if(0<=i<len(grid) and 0<=j<len(grid[0])):
                return True
            return False
        def bfs(i,j,isIslandSet,check):
            queue=collections.deque([])
            queue.append((i,j))
            isIslandSet.add((i,j))
            grid[i][j]=-1
            while(queue):
                x,y=queue.popleft()
                for i in directions:
                    row=x+i[0]
                    col=y+i[1]
                    if(checkValid(row,col) and grid[row][col]==check):
                        queue.append((row,col))
                        grid[row][col]=-1
                        isIslandSet.add((row,col))

                
        def findSecond(i,j,firstSet):
            queue=collections.deque([(i,j,0) for i,j in firstSet])
            while(queue):
                x,y,count=queue.popleft()
            
                for i in directions:
                    row=x+i[0]
                    col=y+i[1]
                    if(checkValid(row,col)):
                        if(grid[row][col]==1):
                            return count
                        elif(grid[row][col]==-1):
                            queue.append((row,col,count))
                            grid[row][col]=2
                        elif(grid[row][col]==0):
                            queue.append((row,col,count+1))
                            grid[row][col]=2


        def solve():
            firstSet=set()
            firstIslandFlag=0
            sX,sY=None,None
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if(grid[i][j]==1):
                        sX,sY=i,j
                        bfs(i,j,firstSet,1)
                        firstIslandFlag=1
                        break
                if(firstIslandFlag):
                    break
            
            return findSecond(sX,sY,firstSet)
    
        return solve()

# Time Complexity O(n^2) SPace COmplexity O(N^2)

                
        
