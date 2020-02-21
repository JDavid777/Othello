import copy
import json

from Game import Game
from Utilities import Utilities
from alphabeta_search import alphabeta_search


class Othello(Game):

    def __init__(self, state):
        self.board = state
        self.turn = 0
        self.utilities = Utilities()
        self.result_operation = []
        self.num_white = 2
        self.num_black = 2

    def set_board(self, board):
        self.board = board

    def actions(self, state):
        list_actions = []
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] is self.turn:
                    pos = [i, j]
                    items = self.validate_move(pos)
                    for k in items:
                        list_actions.append(k)
        return list_actions

    def result(self, state, move):
        print("turno", self.turn)
        print(self.result_operation)
        for i in range(len(self.result_operation)):
            if self.exist(self.result_operation[i], move):
                for j in range(len(self.result_operation[i])):
                    item = (self.result_operation[i][j][0], self.result_operation[i][j][1])
                    state[item[0]][item[1]] = self.turn
                    if self.num_black+self.num_white is 64:
                        if self.num_white>self.num_black:
                            print("Juego terminado ganador",self.num_white)
                        elif self.num_black>self.num_white:
                            print("Juego terminado ganador", self.num_black)
                        else:
                            print("Empate")

        return copy.deepcopy(state)

    def utility(self, state, player):
        point = 0
        with open("TableOfValues.json", "r") as table_data:
            data = json.load(table_data)
        value_table = data["values"]
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] is player:
                    point = point + value_table[i][j]
        return point

    def terminal_test(self, state, depth):
        flag = False
        if depth is 1:
            return True
        return flag

    def to_move(self):
        return self.turn

    def set_move(self, turn):
        self.turn = turn

    def display(self):
        return self.board

    def __repr__(self):
        pass

    def play_game(self):
        pos = alphabeta_search(copy.deepcopy(self.board), self)
        return self.result(self.board, pos)

    def game_user(self, pos):
        new_state = []
        list = self.actions(self.board)
        for i in list:
            if i[0] is pos[0] and i[1] is pos[1]:
                new_state = self.result(self.board, pos)
        return new_state

    def validate_move(self, pos):
        row_and_column = self.utilities.row_and_column(pos, self.board[:])
        diagonals = self.utilities.diagonals(pos, self.board[:])
        row = row_and_column[0]
        column = row_and_column[1]
        diag1 = diagonals[0]
        diag2 = diagonals[1]

        idx1 = self.get_item(row, pos)
        idx2 = self.get_item(column, pos)
        idx3 = self.get_item(diag1, pos)
        idx4 = self.get_item(diag2, pos)
        list_moves = []
        if pos[1] > 1:
            list_moves.append(self.left(row[:idx1]))
            list_moves.append(self.left(column[:idx2]))
            list_moves.append(self.left(diag1[:idx3]))
            list_moves.append(self.left(diag2[:idx4]))
        if idx1 < len(self.board[0]):
            list_moves.append(self.right(row[idx1 + 1:]))
        else:
            list_moves.append(self.right(column[idx1:]))
        if idx2 < len(self.board[0]):
            list_moves.append(self.right(column[idx2 + 1:]))
        else:
            list_moves.append(self.right(column[idx2:]))
        if idx3 < len(self.board[0]):
            list_moves.append(self.right(column[idx2 + 1:]))
        else:
            list_moves.append(self.right(column[idx3:]))
        if idx4 < len(self.board[0]):
            list_moves.append(self.right(column[idx4 + 1:]))
        else:
            list_moves.append(self.right(column[idx4:]))

        new_list = []
        for i in list_moves:
            if len(i) is not 0:
                new_list.append(i[0])
        return new_list

    def left(self, list):
        list.reverse()
        return self.right(list)

    def right(self, list):
        candidates_to_paint = []
        move = []
        if len(list) is not 0:
            pos = list[0]
            aux = self.board[pos[0]][pos[1]]
            if aux is not self.turn and aux is not 0:
                for i in range(1, len(list)):
                    item = (list[i][0], list[i][1])
                    candidates_to_paint.append(item)
                    if self.board[list[i][0]][list[i][1]] is not self.turn:
                        if self.board[list[i][0]][list[i][1]] is 0:
                            candidates_to_paint.append(item)
                            candidates_to_paint.append((pos[0], pos[1]))
                            self.result_operation.append(candidates_to_paint)
                            move.append(item)

                            break
                    else:
                        break
        return move

    def get_item(self, list, item):
        idx = 0
        for i in range(len(list)):

            if list[i][0] == item[0] and list[i][1] is item[1]:
                idx = i
                break
        return idx

    def exist(self, list, element):
        flag = False
        for i in range(len(list)):
            if list[i][0] is element[0] and list[i][1] is element[1]:
                flag = True
        return flag

    def get_black(self):
        return self.num_black

    def get_white(self):
        return self.num_white

    def get_points(self):
        white = 0
        black = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] is 1:
                    black = black + 1
                elif self.board[i][j] is 2:
                    white = white + 1
        self.num_white = white
        self.num_black = black

