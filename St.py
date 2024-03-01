# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:52:08 2024

@author: someone
"""
from Board import *

class St:
    opened_text = "Opened: " + str(Board.opened_current) + "/" + str(Board.opened_max)
    
    
    flags_current = 0
    flags_max = Board.MINES
    flags_text = "Flags: " + str(flags_current) + "/" + str(flags_max)
    

    

    """class pred_flags:
        cells = GetCells()
        def get_cells():
            List = CellsToList(St.pred_flags.cells)
            return List

    class floating:
        cells = GetCells()
        def update_cells():
            for Cell, opened in St.opened.cells.items():
                for neighbor in GetNeighbor(Cell):
                    if St.opened.cells[neighbor] == 1:
                        opened +=1
                if opened == 0:
                    St.floating.cells[Cell] = 1
                else:
                    St.floating.cells[Cell] = 0
                    
        def get_cells():
            St.floating.update_cells()
            List = CellsToList(St.floating.cells) 
            return List
        
    class adjacent:
        cells = GetCells()
        
        def update_cells():
            for Cell, opened in St.opened.cells.items():
                neighboropened = False
                if opened == 0:
                    for neighbor in GetNeighbor(Cell):
                        if St.opened.cells[neighbor] == 1:
                            neighboropened = True
                if neighboropened:
                    St.adjacent.cells[Cell] = 1
                else:
                    St.adjacent.cells[Cell] = 0
                    
        def get_cells():
            St.adjacent.update_cells()
            List = CellsToList(St.adjacent.cells)
            return List
            

    class adjopened:
        cells = GetCells()
        
        def update_cells():
            for Cell, opened in St.opened.cells.items():
                neighborhidden = False
                if opened == 1:
                    for neighbor in GetNeighbor(Cell):
                        if St.opened.cells[neighbor] == 0 and St.pred_flags.cells[neighbor] == 0:
                            neighborhidden = True
                if neighborhidden:
                    St.adjopened.cells[Cell] = 1
                else:
                    St.adjopened.cells[Cell] = 0
                        
        def get_cells():
            St.adjopened.update_cells()
            List = CellsToList(St.adjopened.cells)
            return List
    class progress:
        cells = GetCells()
        def update_cell(Cell):
            St.progress.cells[Cell] = 1"""