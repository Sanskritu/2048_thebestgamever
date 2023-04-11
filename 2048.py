# importing libraries
from tkinter import *
import random

# creating main class
class Play_2048(Tk):
    # adding class variables
    game_board = []
    new_random_tiles = [2, 2, 2, 2, 2, 2, 4]
    score = 0
    high_score = 0
    highest_score = 0
    
    # creating user window
    def __init__ (self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # create user interface
        self.game_score = StringVar(self)
        self.game_score.set("0")
        self.highest_score = StringVar(self)
        self.highest_score.set("0")
        
        # adding new game, score and highest score option
        self.button_frame = Frame(self)
        self.button_frame.grid(row=2, column=0, columnspan =4)
        Button(self.button_frame, text="New Game", font=("times new roman", 15), command=self.new_game).grid(row=0, column =0)
        self.button_frame.pack(side="top")
        
        Label(self.button_frame, text="Score:", font=("times new roman", 15)).grid(row=0, column=1)
        Label(self.button_frame, textvariable=self.game_score, font=("times new roman", 15)).grid(row=0, column=2)
        Label(self.button_frame, text="Record:", font=("times new roman", 15)).grid(row=0, column=3)
        Label(self.button_frame, textvariable=self.highest_score, font=("times new roman", 15)).grid(row=0, column=4)
            
        self.canvas = Canvas(self, width=410, height=410, borderwidth=5, highligtthickness=0) 
        self.canvas.pack(side="top", fill="both", expand="false")

        # create new game

        # add new tiles
    def new_tiles(self):
        index = random.randint(0, 6)
        x = -1
        y = -1

        # ==== check while game is not over
        while self.full() is False:
            x = random.randint(0, 3)
            y = random.randint(0, 3)

            if (self.game_board[x][y] == 0):
                self.game_board[x][y] = self.new_random_tiles[index]
                x1 = y * 105
                y1 = x * 105
                x2 = x1 + 105 - 5
                y2 = y1 + 105 - 5
                num = self.game_board[x][y]
                if num == 2:
                    self.square[x, y] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#e0f2f8", tags="rect",
                                                                    outline="", width=0)
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, font=("Arial", 36), fill="#f78a8a", text="2")
                elif num == 4:
                    self.square[x, y] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#b8dbe5", tags="rect",
                                                                    outline="", width=0)
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, font=("Arial", 36), fill="#f78a8a", text="4")

                break

    
    # check board is full or not
    def full(self):
        for i in range(0, 4):
            for j in range(0, 4):
                if (self.game_board[i][j] == 0):
                    return False
        return True

    # showing game board
    def show_board(self):
        cellwidth = 105
        cellheight = 105
        self.square = {}

        for column in range(4):
            for row in range(4):
                x1 = column * cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth - 5
                y2 = y1 + cellheight - 5
                num = self.game_board[row][column]
                if num == 0:
                    self.show_number0(row, column, x1, y1, x2, y2)
                else:
                    self.show_number(row, column, x1, y1, x2, y2, num)

    # show board block when it is empty
    def show_number0(self, row, column, a, b, c, d):
        self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill="#f5f5f5", tags="rect", outline="")

    # show board number
    def show_number(self, row, column, a, b, c, d, num):
        bg_color = {'2': '#eee4da', '4': '#ede0c8', '8': '#edc850', '16': '#edc53f', '32': '#f67c5f', '64': '#f65e3b', '128': '#edcf72', '256': '#edcc61', '512': '#f2b179', '1024': '#f59563', '2048': '#edc22e',}
        color = {'2': '#776e65', '4': '#f9f6f2', '8': '#f9f6f2', '16': '#f9f6f2', '32': '#f9f6f2', '64': '#f9f6f2', '128': '#f9f6f2', '256': '#f9f6f2', '512': '#776e65', '1024': '#f9f6f2', '2048': '#f9f6f2', }
        self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill=bg_color[str(num)], tags="rect", outline="")
        self.canvas.create_text((a + c) / 2, (b + d) / 2, font=("Arial", 36), fill=color[str(num)], text=str(num))

    # move by user


    # create new game
    def new_game(self):
        self.score = 0
        self.game_score.set("0")
        self.game_board = []
        self.game_board.append([0, 0, 0, 0])
        self.game_board.append([0, 0, 0, 0])
        self.game_board.append([0, 0, 0, 0])
        self.game_board.append([0, 0, 0, 0])
        while True:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if (self.game_board[x][y] == 0):
                self.game_board[x][y] = 2
                break

        index = random.randint(0, 6)
        while self.full() == False:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if (self.game_board[x][y] == 0):
                self.game_board[x][y] = self.new_random_tiles[index]
                break
        self.show_board()

    # check for game over


    # check for game over


    # ==== check for game won
    def game_won(self):
        gameover = [["Y", "O", "U", "", ], ["", "", "", ""], ["W", "O", "N", "!"], ["", "", "", ""]]
        cellwidth = 105
        cellheight = 105
        self.square = {}
        for column in range(4):
            for row in range(4):
                a = column * cellwidth
                b = row * cellheight
                c = a + cellwidth - 5
                d = b + cellheight - 5
                self.square[row, column] = self.canvas.create_rectangle(a, b, c, d, fill="#ede0c8", tags="rect",
                                                                        outline="")
                self.canvas.create_text((a + c) / 2, (b + d) / 2, font=("Arial", 36), fill="#494949",
                                        text=gameover[row][column])



    # main 
    # as in window 