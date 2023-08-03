from typing import List

delta = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def is_valid(board, x,y):
    if x<0: return False
    if y<0: return False
    if x>len(board)-1: return False
    if y>len(board[0])-1:return False
    return True

def adj_mine(board,x,y):
    ans = 0
    for del_x,del_y in delta:
        x_adj = x + del_x
        y_adj = y + del_y
        if is_valid(board, x_adj, y_adj) and board[x_adj][y_adj] == "M":
            ans += 1
    return ans

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == "M": board[x][y] = "X"
        elif board[x][y] == "E":
            queue = []
            num_mine = adj_mine(board, x, y)
            if num_mine == 0: 
                queue.append((x, y))
                board[x][y] = "B"
            else:
                board[x][y] = str(num_mine)
            i_start = 0
            i_end = len(queue)-1
            while i_start<=i_end:
                for x,y in queue[i_start:i_end+1]:
                    for del_x,del_y in delta:
                        x_adj = x + del_x
                        y_adj = y + del_y
                        if is_valid(board, x_adj, y_adj) and (board[x_adj][y_adj] == "E"):
                            num_mine = adj_mine(board, x_adj, y_adj)
                            if num_mine == 0: 
                                queue.append((x_adj, y_adj))
                                board[x_adj][y_adj] = "B"
                            else:
                                board[x_adj][y_adj] = str(num_mine)
                i_start = i_end+1
                i_end = len(queue)-1
        return board


print(
    Solution().updateBoard(
        board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],
        click = [3,0]
    )
)