# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:24:57 2024

@author: someone
"""

import tkinter as tk
from PIL import ImageTk, Image
import datetime

from Board import *
from St import *
from A1 import *


def GetWindowGeometry():
    x = Board.GRID_SIZE * Board.WIDTH + 300
    
    y = Board.GRID_SIZE * Board.HEIGHT
    if y < 200:
        y = 200
    geometry = str(x) + "x" + str(y)
    return geometry

def onclick_tile(event):
    ScreenPos = (event.x,event.y)
    Cell = ScreenPosToCell(ScreenPos)
    Board.CheckFirstClick(Cell)
    
    if Board.board["opened"][Cell] == 0:
        revealed_tile = Open_tile(Cell)
        print("Move " + str(Cell) + ",Revealed " + str(revealed_tile))
        filename = GetFilename(Cell)
        Overlay_tile(Cell,filename)
        update_Label()
        
def onclick_Button_floating():
    Clear_Overlays()
    for Cell in Board.GetFloatingCells():
        Overlay_tile(Cell,"green_tile")
    
def onclick_Button_adjacent():
    Clear_Overlays()
    for Cell in Board.GetAdjacentCells():
        Overlay_tile(Cell,"blue_tile")

def onclick_Button_opened():
    Clear_Overlays()
    for Cell in Board.GetOpenedCells():
        Overlay_tile(Cell,"yellow_tile")

def onclick_Button_adjopened():
    Clear_Overlays()
    for Cell in Board.GetAdjopenedCells():
        Overlay_tile(Cell,"magenta_tile")


def onclick_Button_A0():
    A0.A0()
    if A0.no_of_revealed_tiles == 0:
        A0.random_move()
    for Cell in GetCandidates(Board.board["pred_flags"],1):
        if Cell not in imgs.storage["red_tile"].keys():
            Overlay_tile(Cell,"red_tile")
    for Cell in A0.tiles_to_open:
        filename = GetFilename(Cell)
        Overlay_tile(Cell,filename)
    update_Label()


def onclick_Button_A1():
    A1.A1()
    for Cell in GetCandidates(Board.board["pred_flags"],1):
        if Cell not in imgs.storage["red_tile"].keys():
            Overlay_tile(Cell,"red_tile")
    for Cell in A1.tiles_to_open:
        filename = GetFilename(Cell)
        Overlay_tile(Cell,filename)
    update_Label()


def onclick_Button_Potentiallysafe():
    Clear_Overlays()
    for Cell in Board.GetPotentiallysafeCells():
        Overlay_tile(Cell,"white_tile")


def onclick_Button_GetLogicChain():
    Cell = Entries["GetLogicChain"].get().split(",")
    Cell[0] = int(Cell[0])
    Cell[1] = int(Cell[1])
    Cell = tuple(Cell)

    LogicChain = A2.GetLogicChain(Cell)
    print(LogicChain)

def onclick_Button_GetLogicChains():
    A2.ResetLogicChains()
    A2.GetLogicChains()
    print("Current Logic Chains:")
    print(A2.LogicChains)
    
    A2.FindNewLogicChains()
    print(A2.New_LogicChains)

def onclick_Button_A2():
    A2.A2()
    for Cell in GetCandidates(Board.board["pred_flags"],1):
        if Cell not in imgs.storage["red_tile"].keys():
            Overlay_tile(Cell,"red_tile")
    for Cell in A2.tiles_to_open:
        filename = GetFilename(Cell)
        Overlay_tile(Cell,filename)
    update_Label()


def onclick_Button_Candidates():
    candidates = GetCandidates()
    Clear_Overlays()
    for Cell in candidates:
        Overlay_tile(Cell,"white_tile")
    print(len(candidates))
    
    
    
        
def ScreenPosToCell(ScreenPos):
    x = ScreenPos[0] // Board.GRID_SIZE
    y = ScreenPos[1] // Board.GRID_SIZE
    return (x,y)

def CellToScreenPos(Cell):
    x = Cell[0] * Board.GRID_SIZE
    y = Cell[1] * Board.GRID_SIZE
    return (x,y)
    


def Hotkey_exit(event):
    root.destroy()


FrameWidth = Board.GRID_SIZE * Board.WIDTH
FrameHeight = Board.GRID_SIZE * Board.HEIGHT

root = tk.Toplevel()
root.geometry(GetWindowGeometry())
root.bind('<Escape>',Hotkey_exit)

Frame = tk.Frame(root)
Frame.config(width=FrameWidth, height=FrameHeight, bg="#DFDFDF")
Frame.place(x=0,y=0)

Frame2 = tk.Frame(root)
Frame2.config(width=300,height=max(FrameHeight,200))
Frame2.place(x=FrameWidth,y=0)


Canvas = tk.Canvas(Frame)
Canvas.config(width=FrameWidth, height=FrameHeight, bg="#DFDFDF")
Canvas.place(x=0,y=0,anchor = "nw")
Canvas.bind('<Button-1>',onclick_tile)

Label_St = {}
Buttons = {}
Entries = {}

Label_St["opened"] = tk.Label(Frame2,text=St.opened_text, font=("Verdana",12))
Label_St["opened"].place(x=100,y=100, anchor = "center")

Label_St["flags"] = tk.Label(Frame2,text=St.flags_text, font=("Verdana",12))
Label_St["flags"].place(x=100,y=130, anchor = "center")



Buttons["floating"] = tk.Button(Frame2, text="Floating",width=7,command=onclick_Button_floating)
Buttons["floating"].place(x=50,y=20,anchor="center")

Buttons["adjacent"] = tk.Button(Frame2, text="Adjacent",width=7,command=onclick_Button_adjacent)
Buttons["adjacent"].place(x=120,y=20,anchor="center")

Buttons["opened"] = tk.Button(Frame2, text="Opened",width=7,command=onclick_Button_opened)
Buttons["opened"].place(x=180,y=20,anchor="center")

Buttons["adjopened"] = tk.Button(Frame2, text="AdjOpened",width=9,command=onclick_Button_adjopened)
Buttons["adjopened"].place(x=250,y=20,anchor="center")


Buttons["A0"] = tk.Button(Frame2, text="A0",width=5,command=onclick_Button_A0)
Buttons["A0"].place(x=50,y=50,anchor="center")

Buttons["A1"] = tk.Button(Frame2, text="A1",width=5,command=onclick_Button_A1)
Buttons["A1"].place(x=120,y=50,anchor="center")

Buttons["Potentiallysafe"] = tk.Button(Frame2, text="Potentiallysafe",width=13,command=onclick_Button_Potentiallysafe)
Buttons["Potentiallysafe"].place(x=220,y=50,anchor="center")

Entries["GetLogicChain"] = tk.Entry(Frame2,width=8)
Entries["GetLogicChain"].insert(0,"0,0")
Entries["GetLogicChain"].place(x=20,y=160)

Buttons["GetLogicChain"] = tk.Button(Frame2, text="GetLogic",width=8,command=onclick_Button_GetLogicChain)
Buttons["GetLogicChain"].place(x=80,y=160)

Buttons["GetLogicChain"] = tk.Button(Frame2, text="GetLogics",width=8,command=onclick_Button_GetLogicChains)
Buttons["GetLogicChain"].place(x=150,y=160)

Buttons["A2"] = tk.Button(Frame2, text="A2",width=5,command=onclick_Button_A2)
Buttons["A2"].place(x=220,y=160)


from imgs import *


def StartNewGame():
    Board.ResetBoard_Rd()
    for y in range(Board.HEIGHT):
        for x in range(Board.WIDTH):
            Cell = (x,y)
            ScreenPos = CellToScreenPos(Cell)
            imgs.storage[Cell] = Canvas.create_image(ScreenPos[0],ScreenPos[1],anchor = "nw",image=imgs.imgs["tile"])

StartNewGame()
print(GetBoardString())


def GetFilename(Cell):
    if Board.board["MINES"][Cell] == 1:
        filename = "flag"
    else:
        number = Board.GetNumber(Cell)
        filename = "num" + str(number)
    return filename

def Overlay_tile(Cell,filename):
    ScreenPos = CellToScreenPos(Cell)
    imgs.storage[filename][Cell] = Canvas.create_image(ScreenPos[0],ScreenPos[1],anchor = "nw",image=imgs.imgs[filename],tag=filename)

def ClearOverlay(Cell,filename):
    Canvas.delete(imgs.storage[filename][Cell])
    
def Clear_Overlays():
    for filename in ["green_tile","blue_tile","yellow_tile","magenta_tile","white_tile"]:
        Canvas.delete(filename)
        imgs.storage[filename] = {}
        
        
def update_Label():
    St.opened_text = "Opened: " + str(Board.opened_current) + "/" + str(Board.opened_max)
    Label_St["opened"].config(text=St.opened_text)

    St.flags_text = "Flags: " + str(St.flags_current) + "/" + str(St.flags_max)
    Label_St["flags"].config(text=St.flags_text)

       


root.mainloop()