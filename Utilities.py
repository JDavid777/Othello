class Utilities:

    def __init__(self):
        self

    def aux_diagonal(self, pos, board, orientation):
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
                if x is 0 or x is len(board)-1 or y is 0 or y is len(board)-1:
                    break
                x = x - 1
                y = y + 1
        new_pos = (x, y)
        return new_pos

    def diagonals(self, pos, board):
        diag1 = self.diagonal(pos, board, True)
        diag2 = self.diagonal(pos, board, False)
        return (diag1, diag2)

    def diagonal(self, pos, board, orientation):
        diagonal = []
        new_pos = self.aux_diagonal(pos, board, orientation)
        x = new_pos[0]
        y = new_pos[1]
        for i in range(len(board)):
            if x < len(board[0]) and y >= 0 :
                diagonal.append((x,y))
            if orientation:
                x = x + 1
                y = y + 1
            else:
                x = x + 1
                y = y - 1
        return diagonal

    def row_and_column(self, pos, board):
        vertical = []
        horizontal = []
        for i in range(len(board)):
            vertical.append((i,pos[1]))
            horizontal.append((pos[0],i))
        return horizontal, vertical
