# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:31:26 2018

@author: eumartinez

"""
import copy
import json
from tkinter import *
from Othello import Othello
from alphabeta_search import alphabeta_search


class App:

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.height = 400
        self.width = 400
        self.grid_column = 8
        self.grid_row = 8
        self.canvas = Canvas(self.frame, height=self.height, width=self.width)
        self.cellwidth = int(self.canvas["width"]) / self.grid_column
        self.cellheight = int(self.canvas["height"]) / self.grid_row
        self.draw_grid()
        self.canvas.pack()

        with open("board.json", "r") as boar_data:
            board = json.load(boar_data)
            self.model = board["board"]
        self.player = 1
        self.pos = (0, 0)
        self.draw_chips()
        self.game = Othello(copy.deepcopy(self.model))
        self.machine = Label(self.frame, text="CPU 2")
        self.machine.pack(side=LEFT)
        self.player1 = Label(self.frame, text="Player1 2")
        self.player1.pack(side=RIGHT)

        def handler(event, self=self):
            return self.__on_click(event)

        self.canvas.bind('<Button-1>', handler)

        self.hi_there = Button(self.frame, text="Jugar", command=self.start_game)
        self.hi_there.pack(side=LEFT)

    def draw_grid(self):
        for i in range(self.grid_row):
            for j in range(self.grid_column):
                x1 = i * self.cellwidth
                y1 = j * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")

    def draw_chip(self):
        x = self.pos[1] * self.cellwidth
        y = self.pos[0] * self.cellheight
        if self.player == 1:
            self.canvas.create_oval(x, y, x + self.cellwidth, y + self.cellheight, fill='black')
            self.player = 2
        else:
            self.canvas.create_oval(x, y, x + self.cellwidth, y + self.cellheight, fill='white')
            self.player = 1

    def draw_chips(self):
        white = 0
        black = 0
        for i in range(len(self.model)):
            row = self.model[i]
            for j in range(len(row)):
                val = self.model[i][j]
                x = j * self.cellwidth
                y = i * self.cellheight
                if val == 1:
                    white += 1
                    self.canvas.create_oval(x, y, x + self.cellwidth, y + self.cellheight, fill='black')
                elif val == 2:
                    black += 1
                    self.canvas.create_oval(x, y, x + self.cellwidth, y + self.cellheight, fill='white')


    def set_points(self, white, black):
        txt1 = StringVar()
        txt1.set("CPU: " + str(black))
        self.machine.config(textvariable=txt1)
        txt2 = StringVar()
        txt2.set("Player: " + str(white))
        self.player.config(textvariable=txt2)

    def __on_click(self, event):

        i = int(event.y / self.cellheight)
        j = int(event.x / self.cellwidth)
        self.pos = (i, j)
        if self.model[i][j] == 0:
            self.model[i][j] = self.player
            self.player = 1
            new_state = self.game.game_user(self.pos)
            if len(new_state) is not 0:
                self.model = new_state
                self.game.result_operation = []
                self.player = 1
                self.game.set_move(self.player)
                self.draw_chips()
                self.start_game()

    def start_game(self):
        self.game.set_move(self.player)
        self.model = self.game.play_game()
        self.game.result_operation = []
        self.player = 2
        self.game.set_move(self.player)
        self.draw_chips()


root = Tk()
board = App(root)
root.mainloop()
