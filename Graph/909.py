class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def getCords(i,n):
            div=i//n
            mod=i%n
            if(mod!=0):
                x=n-1-div
            else:
                x=n-div

            if((n-x)%2==1):
                y=n-1 if mod==0 else mod-1
            else:
                y=0 if mod==0 else n-mod
            return x,y

        def bfs():

            q = deque()
            q.append([1, 0])  # [square, moves]
            visit = set()
            n=len(board)
            while q:
                print(q)
                square, moves = q.popleft()
                for i in range(1, 7):
                    nextSquare = square + i
                    r, c = getCords(nextSquare,n)
                    if board[r][c] != -1:
                        nextSquare = board[r][c]
                    if nextSquare == n * n:
                        return moves + 1
                    if nextSquare not in visit:
                        visit.add(nextSquare)
                        q.append([nextSquare, moves + 1])
        
                            
            return -1
        return bfs()
                

#  Time Complexity O(n^2) space COmplexity O(n)
