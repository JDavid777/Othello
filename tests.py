
def aux_diagonal( pos, board, orientation):
    x = pos[0]
    y = pos[1]
    flag = True
    if orientation:
        while flag:
            if x is 0 or y is 0:
                break
            x = x - 1
            y = y - 1
    else:
        while flag:
            if x is 0 or x is len(board) - 1 or y is 0 or y is len(board) - 1:
                break
            x = x - 1
            y = y + 1
    new_pos = (x, y)
    return new_pos

def diagonals(pos, board):
    diag1 = diagonal(pos, board, True)
    diag2 = diagonal(pos, board, False)
    return (diag1, diag2)


def diagonal( pos, board, orientation):
    diagonal = []
    new_pos = aux_diagonal(pos, board, orientation)
    x = new_pos[0]
    y = new_pos[1]
    for i in range(len(board)):
        if x < len(board[0]) and y >= 0:
            diagonal.append((x, y))
        if orientation:
            x = x + 1
            y = y + 1
        else:
            x = x + 1
            y = y - 1
    return diagonal

def row_and_column( pos, board):
    vertical = []
    horizontal = []
    for i in range(len(board)):
        vertical.append((i, pos[1]))
        horizontal.append((pos[0], i))
    return horizontal, vertical

board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

pos = (3, 2)
diag=diagonals(pos,board)
diag1=diag[0]
diag2=diag[1]
print(diag1)
print(diag2)
rc=row_and_column(pos,board)
r=rc[0]
c=rc[1]
print(r)
print(c)
"""
diagonals(pos, board)

side(pos,board)
board.reverse()


validate_move(1 ,pos ,board)"""


def result(self, state, move):
    state[move[0]][move[1]] = self.turn
    print("turno", self.turn)
    print(self.result_operation)
    for i in range(len(self.result_operation)):
        if self.result_operation[i][0][0] is move[0] and self.result_operation[i][0][1] is move[1]:
            for j in range(len(self.result_operation[i])):
                item = (self.result_operation[i][j][0], self.result_operation[i][j][1])
                state[item[0]][item[1]] = self.turn
    return copy.deepcopy(state)