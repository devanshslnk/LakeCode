class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def checkValid(i,j):
            if(0<=i<len(grid) and 0<=j<len(grid[0])):
                return True
            return False

        def solve(k):
            q=collections.deque([(0,0,0,k)])
            obCount=[[float("-inf") for i in range(len(grid[0]))]for j in range(len(grid))]
            visited=set()
            visited.add((0,0))
            obCount[0][0]=k
            while(q):
                x,y,moves,currK=q.popleft()
               
                # print(x,y,currK)
                if(x==len(grid)-1 and y==len(grid[0])-1):
                    return moves
                for i in range(4):
                    row=x+directions[i][0]
                    col=y+directions[i][1]
                    if(checkValid(row,col)):
                        if((row,col) not in visited):
                            if(grid[row][col]==1 and currK>0):
                                
                                q.append((row,col,moves+1,currK-1))
                                obCount[row][col]=currK-1
                                visited.add((row,col))

                            elif(grid[row][col]==0):
                                q.append((row,col,moves+1,currK))
                                obCount[row][col]=currK
                                visited.add((row,col))
                        else:
                            if(grid[row][col]==1 and currK>0 and  obCount[row][col]<currK-1):                                
                                q.append((row,col,moves+1,currK-1))
                                obCount[row][col]=currK-1

                            elif(grid[row][col]==0 and obCount[row][col]<currK):
                                q.append((row,col,moves+1,currK))
                                obCount[row][col]=currK
            return -1
        return solve(k)

# O(m.n.k) SC O(n.m)

