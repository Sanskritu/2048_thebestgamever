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
        self.new_game()

    # add new tiles
    def new_tiles(self):
        index = random.randomint(0, 6)
        x = -1
        y = -1
        
        # check while game is not over
        while self.full()== False:
            x = random.radiant(0, 3)
            y = random.radiant(0, 3)
            
            if (self.game_board[x][y]== 0):
                self.game_board[x][y] = self.new_random_tiles[index]
                x1 = y* 105
                y1 = x * 105
                x2 = x1 + 105 -5
                y2 = y1 +105 -5
                num = self.game_board[x][y]
                if num == 2:
                    self.square[x, y] = self.canvas.create_rectangle(x1, y1, x2, y2, fill = "#e0f2f8", tags="rect", outline="", width=0)
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2, font=("Ariel", 36), fill="#f78a8a", text ="2")
                elif num==4:
                    self.square[x, y] = self.canvas.create_rectangle(x1, y1, x2, y2, fill = "#b8dbe5", tags="rect", outline="", width=0)
                    self.canvas.create_text((x1+x2)/2, (y1+y2)/2, font=("Ariel", 36), fill="#f78a8a", text ="4")
                break
            
        # check board is full or not
        
