class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def checkValid(i,j):
            if(0<=i<len(grid1) and 0<=j<len(grid1[1])):
                return True
            return False
        def bfs(i,j):
            q=collections.deque([])
            q.append((i,j))
            grid2[i][j]=-1
            ans=True
            while(q):
                x,y=q.popleft()
                # print(x,y,grid1[x][y])
                if(grid1[x][y]!=1):
                    ans=False
                for k in directions:
                    row=x+k[0]
                    col=y+k[1]
                    if(checkValid(row,col) and grid2[row][col]==1):
                        q.append((row,col))
                        grid2[row][col]=-1

            return ans

        def solve():
            ans=0
            for i in range(len(grid2)):
                for j in range(len(grid2[i])):
                    if(grid2[i][j]==1):
                        if(bfs(i,j)):
                            ans+=1
                        

            return ans

        return solve()


        # Time Complexity O(n^2) Space COmplexity O(N^2)
