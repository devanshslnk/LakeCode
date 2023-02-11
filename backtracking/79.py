class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkValid(i,j):
            if(0<=i<len(board) and 0<=j<len(board[0])):
                return True
            return False
        def backtracking(curr,i,j):
            if(curr==len(word)):
                # print(curr)
                return True
            if(checkValid(i,j) and board[i][j]==word[curr]):
                temp=board[i][j]
                board[i][j]=None
                if(backtracking(curr+1,i+1,j) or backtracking(curr+1,i-1,j) or backtracking(curr+1,i,j+1) or 
backtracking(curr+1,i,j-1)):
                    return True
                board[i][j]=temp
            return False



        

        def solve():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if(backtracking(0,i,j)):
                        return True
            return False


        return solve()

#  TC O(n^2) SC O(n)
