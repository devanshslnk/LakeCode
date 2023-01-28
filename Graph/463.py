class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def checkValidity(i,j):
            if(0<=i<len(grid) and 0<=j<len(grid[0])):
                return True
            return False
        
        def bfs(i,j):
            #  Do bfs here
            queue=collections.deque([])
            queue.append((i,j))
            grid[i][j]=-1
            localPeri=0
            while(queue):
                x,y=queue.popleft()
                surrounding=0
                for i in directions:
                    row=x+i[0]
                    col=y+i[1]
                    if(checkValidity(row,col) and grid[row][col]==1):
                        queue.append((row,col))
                        grid[row][col]=-1
                    elif(not checkValidity(row,col) or grid[row][col]==0):
                        surrounding+=1
                localPeri+=surrounding
            return localPeri
        def solve():
            ans=0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if(grid[i][j]==1):
                        ans+=bfs(i,j)
            return ans
        return solve()

# Time Complexity O(n^2) Space Complexity O(n^2)
