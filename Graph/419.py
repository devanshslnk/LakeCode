class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        directions=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
        def checkValid(i,j):
            if(0<=i<len(board) and 0<=j<len(board[0])):
                return True
            return False

        def bfs(i,j,visited,direction):
            visited.add((i,j))
            q=collections.deque()
            q.append((i,j))
            ans=1
            while(q):
                x,y=q.popleft()
                for d in directions:
                    row=x+d[0]
                    col=y+d[1]
                    if(checkValid(row,col) and (row,col) not in visited and board[row][col]=="X"):
                        if(d!=direction):
                            ans=0
                        q.append((row,col))
                        visited.add((row,col))
            return ans
                        



        def checkDirection(i,j):
            for d in directions[1:]:
                row=i+d[0]
                col=j+d[1]
                if(checkValid(row,col) and board[row][col]=="X"):
                    return d
            return (0,0)


        def solve():
            count=0
            visited=set()
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(board[i][j]=="X" and (i,j) not in visited):
                        direction=checkDirection(i,j)
                        count+=bfs(i,j,visited,direction)
            
            return count
        return solve()
# TC O(n^2) SC O(N^2)

        



