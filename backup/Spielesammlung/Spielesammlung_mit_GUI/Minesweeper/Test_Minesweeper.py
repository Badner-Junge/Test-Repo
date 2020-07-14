# __author__    = 'Fabian'
# __project__   = erste_Programme
# __file__      = Test_Minesweeper.py
# __version__   =

import tkinter, configparser, random, os, tkinter.messagebox, tkinter.simpledialog

window = tkinter.Tk()

window.title("Minesweeper")

#prepare default values

rows = 10
cols = 10
mines = 10

field = []
buttons = []

colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']

gameover = False
customsizes = []

window.mainloop()