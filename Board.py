# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 13:53:36 2024

@author: someone
"""
import random
import datetime


def GetCells():
    Cells = {}
    for y in range(Board.HEIGHT):
        for x in range(Board.WIDTH):
            Cell = (x,y)
            Cells[Cell] = 0
    return Cells

def GetCandidates(Cells,req_value):
    candidates = []
    for Cell, value in Cells.items():
        if value == req_value:
            candidates.append(Cell)
    return candidates


class Board:
    WIDTH = 30
    HEIGHT = 16
    MINES = 50
    GRID_SIZE = 24
    
    
    board = {"MINES":{},"opened":{},"pred_flags":{},"number":{}}
    IsFirstClick = False
    opened_current = 0
    opened_max = WIDTH * HEIGHT - MINES
    
    
    def ResetBoard_L():
        Board.board = {"MINES":GetCells(),"opened":GetCells(),"pred_flags":GetCells(), "number":GetCells()}
         
        candidates = list(GetCells().keys())
        no_of_candidates = len(candidates)
        for PlacedMines in range(Board.MINES):
            rng = int(random.random() * no_of_candidates)
            Cell = candidates[rng]
            Board.board["MINES"][Cell] = 1
            candidates.remove(Cell)
            no_of_candidates -= 1
    def ResetBoard_Rd():
        Board.opened_current = 0
        Board.opened_max = Board.WIDTH * Board.HEIGHT - Board.MINES
        Board.board = {"MINES":GetCells(),"opened":GetCells(),"pred_flags":GetCells(),"number":GetCells()}
        Board.IsFirstClick = True
        
        PlacedMines = 0
        while PlacedMines < Board.MINES: #PlaceMines
            Rd_x = int(random.random() * Board.WIDTH)
            Rd_y = int(random.random() * Board.HEIGHT)
            Cell = (Rd_x,Rd_y)
            if Board.board["MINES"][Cell] == 0:
                Board.board["MINES"][Cell] = 1
                PlacedMines += 1
        
        
    def CheckFirstClick(Cell):
        if Board.IsFirstClick:
            Board.IsFirstClick = False
            Board.FirstClick_Rd(Cell)
                
    def FirstClick_L(Cell):
        if Board.board["MINES"][Cell] == 1:
            candidates = GetCandidates(Board.board["MINES"],0)
            no_of_candidates = len(candidates)
            rng = int(random.random() * no_of_candidates)
            new_Cell = candidates[rng]
            Board.board["MINES"][new_Cell] = 1
            Board.board["MINES"][Cell] = 0

    def FirstClick_Rd(Cell):
        if Board.board["MINES"][Cell] == 1:
            Rd_x = int(random.random() * Board.WIDTH)
            Rd_y = int(random.random() * Board.HEIGHT)
            new_Cell = (Rd_x,Rd_y)
            while Board.board["MINES"][new_Cell] == 1:
                Rd_x = int(random.random() * Board.WIDTH)
                Rd_y = int(random.random() * Board.HEIGHT)
                new_Cell = (Rd_x,Rd_y)
            Board.board["MINES"][new_Cell] = 1
            Board.board["MINES"][Cell] = 0
            
    def GetNeighbor(Cell):
        x = Cell[0]
        y = Cell[1]
        Neighbor = []
        
        if x == 0 and x == Board.WIDTH-1:
            x_range = [x]
        elif x == 0:
            x_range = [x,x+1]
        elif x == Board.WIDTH-1:
            x_range = [x-1,x]
        else:
            x_range = [x-1,x,x+1]
        
        if y == 0 and y == Board.HEIGHT-1:
            y_range = [y]
        elif y == 0:
            y_range = [y,y+1]
        elif y == Board.HEIGHT-1:
            y_range = [y-1,y]
        else:
            y_range = [y-1,y,y+1]
        
        for y in y_range:
            for x in x_range:
                coord = (x,y)
                if coord != Cell:
                    Neighbor.append(coord)
        
        return Neighbor
    
    
    def GetNumber(Cell):
        Neighbor = Board.GetNeighbor(Cell)
        number = 0
        for Cell in Neighbor:
            number += Board.board["MINES"][Cell]
        return number


    def GetAdjacentCells():
        candidates = []
        for Cell in GetCandidates(Board.board["opened"],0):
            IsAdjacent = False
            for Neighbor in Board.GetNeighbor(Cell):
                if Board.board["opened"][Neighbor] == 1:
                    IsAdjacent = True
            if IsAdjacent:
                candidates.append(Cell)
        return candidates
    
    def GetFloatingCells():
        candidates = []
        for Cell in GetCandidates(Board.board["opened"],0):
            IsFloat = True
            for Neighbor in Board.GetNeighbor(Cell):
                if Board.board["opened"][Neighbor] == 1:
                    IsFloat = False
            if IsFloat:
                candidates.append(Cell)
        return candidates

    def GetOpenedCells():
        return GetCandidates(Board.board["opened"],1)

    def GetAdjopenedCells():
        candidates = []
        for Cell in GetCandidates(Board.board["opened"],1):
            IsAdjopened = False
            for Neighbor in Board.GetNeighbor(Cell):
                if Board.board["opened"][Neighbor] == 0 and Board.board["pred_flags"][Neighbor] == 0:
                    IsAdjopened = True
            if IsAdjopened:
                candidates.append(Cell)
        return candidates

    def GetPotentiallysafeCells():
        candidates = []
        for Cell in GetCandidates(Board.board["opened"],0):
            if Board.board["pred_flags"][Cell] == 0:
                candidates.append(Cell)
        return candidates
        

def Open_tile(Cell):
    if Board.board["opened"][Cell] == 0 and Board.board["pred_flags"][Cell] == 0:
        if Board.board["MINES"][Cell] == 1:
            return "*"
        else:
            Board.board["opened"][Cell] = 1
            Board.opened_current += 1
            number = Board.GetNumber(Cell)
            return number
    
    
def Open_tiles(Cells):
    revealed_tiles = []
    for Cell in Cells:
        revealed_tile = Open_tile(Cell)
        revealed_tiles.append(revealed_tile)
    return revealed_tiles    
    
def GetBoardString():
    string = ""
    for y in range(Board.HEIGHT):
        if y > 0:
            string += "\n"
        for x in range(Board.WIDTH):
            Cell = (x,y)
            if Board.board["MINES"][Cell] == 1:
                string += "*"
            else:
                number = Board.GetNumber(Cell)
                string += str(number)
    return string






