# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:24:57 2024

@author: someone
"""

import tkinter as tk
from PIL import ImageTk, Image

from Board import *
board.board = GetBoard()
PrintBoard()

def GetWindowGeometry():
    x = board.GRID_SIZE * board.WIDTH + 200
    y = board.GRID_SIZE * board.HEIGHT
    geometry = str(x) + "x" + str(y)
    return geometry

def onclick_tile(event):
    ScreenPos = (event.x,event.y)
    Cell = ScreenPosToCell(ScreenPos)
    
    if stat.opened.cells[Cell] == 0:
        OpeningCells = CheckOpening(Cell)
        for Cell in OpeningCells:
            Open_tile(Cell)


def ScreenPosToCell(ScreenPos):
    x = ScreenPos[0] // board.GRID_SIZE
    y = ScreenPos[1] // board.GRID_SIZE
    return (x,y)

def CellToScreenPos(Cell):
    x = Cell[0] * board.GRID_SIZE
    y = Cell[1] * board.GRID_SIZE
    return (x,y)
    


def Hotkey_exit(event):
    root.destroy()


FrameWidth = board.GRID_SIZE * board.WIDTH
FrameHeight = board.GRID_SIZE * board.HEIGHT

root = tk.Toplevel()
root.geometry(GetWindowGeometry())
root.bind('<Escape>',Hotkey_exit)

Frame = tk.Frame(root)
Frame.config(width=FrameWidth, height=FrameHeight, bg="#DFDFDF")
Frame.place(x=0,y=0)

Frame2 = tk.Frame(root)
Frame2.config(width=200,height=FrameHeight)
Frame2.place(x=FrameWidth,y=0)


Canvas = tk.Canvas(Frame)
Canvas.config(width=FrameWidth, height=FrameHeight, bg="#DFDFDF")
Canvas.place(x=0,y=0,anchor = "nw")
Canvas.bind('<Button-1>',onclick_tile)

Label_opened = tk.Label(Frame2,text=stat.opened.text, font=("Verdana",12))
Label_opened.place(x=100,y=100, anchor = "center")

Label_flags = tk.Label(Frame2,text=stat.flags.text, font=("Verdana",12))
Label_flags.place(x=100,y=140, anchor = "center")

from imgs import *

def StartNewGame():
    for y in range(board.HEIGHT):
        for x in range(board.WIDTH):
            Cell = (x,y)
            ScreenPos = CellToScreenPos(Cell)
            imgs.storage[Cell] = Canvas.create_image(ScreenPos[0],ScreenPos[1],anchor = "nw",image=imgs.imgs["tile"])

StartNewGame()

def Open_tile(Cell):
    if stat.opened.cells[Cell] == 0:
        stat.opened.cells[Cell] = 1
        ScreenPos = CellToScreenPos(Cell)
        RevealedTile = GetRevealedTile(Cell)
        if RevealedTile == "*":
            update_stat_flags()
            filename = "flag"
        else:
            update_stat_opened()
            filename = "num" + RevealedTile
        imgs.storage[Cell] = Canvas.create_image(ScreenPos[0],ScreenPos[1],anchor = "nw",image=imgs.imgs[filename])
    
def update_stat_opened():
    stat.opened.current +=1
    stat.opened.text = "Opened: " + str(stat.opened.current) + "/" + str(stat.opened.maximum)
    Label_opened.config(text=stat.opened.text)

def update_stat_flags():
    stat.flags.current +=1
    stat.flags.text = "Flags: " + str(stat.flags.current) + "/" + str(stat.flags.maximum)
    Label_flags.config(text=stat.flags.text)

root.mainloop()