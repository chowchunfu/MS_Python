# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:39:00 2024

@author: someone
"""

from Board import *

def GetHeatmap(no_of_boards):
    heatmap = Board.GetCells()
    
    for board in range(no_of_boards):
        Board.ResetBoard_Rd()
        candidates = Board.GetCandidates(Board.board["MINES"],1)
        
        for Cell in candidates:
            heatmap[Cell] +=1
            
    return heatmap

def GetHeatmap2(no_of_boards):
    heatmap = Board.GetCells()
    
    for board in range(no_of_boards):
        Board.ResetBoard_Rd()
        Board.FirstClick_Rd((0,0))
        candidates = Board.GetCandidates(Board.board["MINES"],1)
        
        for Cell in candidates:
            heatmap[Cell] +=1
            
    return heatmap



H = GetHeatmap2(1000)
m = 0
for Cell,value in H.items():
    m += value
print(H)
print(m)        
        
