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
        self.button_frame.pack(side="bottom")
        
        