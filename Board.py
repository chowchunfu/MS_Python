# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:53:36 2024

@author: someone
"""
import random

class board:
    WIDTH = 30
    HEIGHT = 16
    MINES = 99
    GRID_SIZE = 24
    
    board = {}
    
def GetRandomCoord():
    x = int(board.WIDTH * random.random())
    y = int(board.HEIGHT * random.random())
    return (x,y)

def GetCells():
    Cells = {}
    for y in range(board.HEIGHT):
        for x in range(board.WIDTH):
            Cell = (x,y)
            Cells[Cell] = 0
    return Cells
    
def GetBoard(): # 0 = Not Mine, 1 = Mine
    Board = GetCells()
    PlacedMines = 0
    if board.MINES < 0.8 * board.WIDTH * board.HEIGHT: #Limit Mine Density
        while PlacedMines < board.MINES:
            RandomCoord = GetRandomCoord()
            if Board[RandomCoord] != 1:
                Board[RandomCoord] = 1
                PlacedMines +=1

    return Board

class stat:
    class opened:
        cells = GetCells()
        current = 0
        maximum = board.WIDTH * board.HEIGHT - board.MINES
        text = "Opened: " + str(current) + "/" + str(maximum)
    class flags:
        current = 0
        maximum = board.MINES
        text = "Flags: " + str(current) + "/" + str(maximum) 
        

def GetAdjacentCells(Cell):
    x = Cell[0]
    y = Cell[1]
    AdjacentCells = []
    
    if x == 0:
        x_range = [x,x+1]
    elif x == board.WIDTH-1:
        x_range = [x-1,x]
    else:
        x_range = [x-1,x,x+1]
    
    if y == 0:
        y_range = [y,y+1]
    elif y == board.HEIGHT-1:
        y_range = [y-1,y]
    else:
        y_range = [y-1,y,y+1]
    
    for y in y_range:
        for x in x_range:
            coord = (x,y)
            if coord != Cell:
                AdjacentCells.append(coord)
    
    return AdjacentCells
    
def GetNumber(Cell):
    AdjacentCells = GetAdjacentCells(Cell)
    num = 0
    for Cell in AdjacentCells:
        num += board.board[Cell]
    return num

def GetRevealedTile(Cell):
    if board.board[Cell] == 1:
        return "*"
    else:
        AdjacentCells = GetAdjacentCells(Cell)
        num = 0
        for Cell in AdjacentCells:
            num += board.board[Cell]
        return str(num)

def CheckOpening(Cell):
    if GetRevealedTile(Cell) == "0":
        OpeningCells = []
        GetOpeningCells(Cell,OpeningCells)
        return OpeningCells
    else:
        return [Cell]
    
def GetOpeningCells(Cell,OpeningCells):
    OpeningCells.append(Cell)
    AdjacentCells = GetAdjacentCells(Cell)
    for Cell in AdjacentCells:
        if Cell not in OpeningCells:
            if GetRevealedTile(Cell) == "0":
                GetOpeningCells(Cell,OpeningCells)
            else:    
                OpeningCells.append(Cell)

def PrintBoard():
    string = ""
    for y in range(board.HEIGHT):
        if y > 0:
            string += "\n"
        for x in range(board.WIDTH):
            Cell = (x,y)
            string += GetRevealedTile(Cell)         
    print(string)
    
Board = GetBoard()