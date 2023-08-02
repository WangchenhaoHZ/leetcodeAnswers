from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        o_list = []
        for i in range(len(board)):
            if board[i][0] == "O":
                o_list.append((i,0))
            if board[i][len(board[0])-1] == "O":
                o_list.append((i,len(board[0])-1))
        for i in range(len(board[0])):
            if board[0][i] == "O":
                o_list.append((0,i))
            if board[len(board)-1][i] == "O":
                o_list.append((len(board)-1,i))
        i_start = 0
        i_end = len(o_list)-1
        while i_start <= i_end:
            for x,y in o_list[i_start:i_end+1]:
                if (x - 1 >= 0) and (board[x-1][y] == "O") and (not (x-1,y) in o_list):
                    o_list.append((x-1,y))
                if (x + 1 <= len(board)-1) and (board[x+1][y] == "O") and (not (x+1,y) in o_list):
                    o_list.append((x+1,y))
                if (y - 1 >= 0) and (board[x][y-1] == "O") and (not (x,y-1) in o_list):
                    o_list.append((x,y-1))
                if (y + 1 <= len(board[0])-1) and (board[x][y+1] == "O") and (not (x,y+1) in o_list):
                    o_list.append((x,y+1))
            i_start = i_end + 1
            i_end = len(o_list)-1
        for x, row in enumerate(board):
            for y, char in enumerate(row):
                if not (x,y) in o_list:
                    board[x][y] = "X"
        
        
        print(board)

print(
    Solution().solve(
        board = [["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    )
)