# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:05:15 2024

@author: someone
"""

from Board import *

class Alg:
    A0 = 1



class A0: #First corner and Random guess
    tiles_to_open = set([])
    no_of_revealed_tiles = 0
    def A0():
        A0.tiles_to_open = set([])
        revealed_tiles = A0.openings()
        A0.no_of_revealed_tiles = len(revealed_tiles)

        return revealed_tiles
        
    def first_move(): #First corner move
        firstCell = (0,0)
        Board.CheckFirstClick(firstCell)
        revealed_tile = Open_tile(firstCell)
        print("First Move " + str(firstCell) + ",Revealed " + str(revealed_tile))
        return revealed_tile
        
    
    def random_move(): #Random guess
        A0.tiles_to_open = set([])
        candidates = Board.GetPotentiallysafeCells()
        no_of_candidates = len(candidates)
        randomCell = candidates[int(random.random() * no_of_candidates)]
        A0.tiles_to_open.add(randomCell)
        revealed_tile = Open_tile(randomCell)
        print("Random Move " + str(randomCell) + ",Revealed " + str(revealed_tile))
        return revealed_tile
    
    def openings():
        
        for Cell in Board.GetAdjopenedCells():
            if Board.GetNumber(Cell) == 0:
                for Neighbor in Board.GetNeighbor(Cell):
                    A0.tiles_to_open.add(Neighbor)
        revealed_tiles = Open_tiles(A0.tiles_to_open)
        no_of_revealed_tiles = len(revealed_tiles)
        print("Opening Move, Revealed " + str(no_of_revealed_tiles) + " tiles")
        return revealed_tiles
        
class A1: #Trivial Flag and Chording
    tiles_to_open = set([])
    no_of_revealed_tiles = 0
    no_of_pred_flags = 0
    def A1():
        A1.tiles_to_open = set([])
        A1.no_of_revealed_tiles = 0
        A1.no_of_pred_flags = 0
        
        A1.detect_flags()
         
        for Cell in Board.GetAdjopenedCells():
            A1.chording(Cell)
        
        revealed_tiles = Open_tiles(A1.tiles_to_open)
        A1.no_of_revealed_tiles = len(revealed_tiles)
        
        print("Trivial Move, predicted " + str(A1.no_of_pred_flags) + " flags, revealed " + str(A1.no_of_revealed_tiles) + " tiles")
        
        return revealed_tiles
        
    def detect_flags():
        for Cell in Board.GetAdjopenedCells():
            A1.detect_flag(Cell)
        
    """def detect_flag(Cell):
        satisfaction = 0
        satisfaction += Board.GetNumber(Cell)
        for Neighbor in Board.GetNeighbor(Cell):
            satisfaction += Board.board["opened"][Neighbor]
        
        req_satisfaction = len(Board.GetNeighbor(Cell))
        if satisfaction == req_satisfaction:
            for Neighbor in Board.GetNeighbor(Cell):
                if Board.board["opened"][Neighbor] == 0 and Board.board["pred_flags"][Neighbor] == 0:
                    Board.board["pred_flags"][Neighbor] = 1
                    A1.no_of_pred_flags += 1"""

    def detect_flag(Cell):
        number = Board.GetNumber(Cell)
        no_of_unopened_cell = 0
        for Neighbor in Board.GetNeighbor(Cell):
            if Board.board["opened"][Neighbor] == 0:
                no_of_unopened_cell += 1
        
        if number == no_of_unopened_cell:
            for Neighbor in Board.GetNeighbor(Cell):
                if Board.board["opened"][Neighbor] == 0 and Board.board["pred_flags"][Neighbor] == 0:
                    A1.no_of_pred_flags += 1
            PredFlag_tiles(Board.GetNeighbor(Cell))
        

    def chording(Cell):
        no_of_neighbor_flags = 0
        for Neighbor in Board.GetNeighbor(Cell):
            no_of_neighbor_flags += Board.board["pred_flags"][Neighbor]
        
        if Board.GetNumber(Cell) == no_of_neighbor_flags:
            for Neighbor in Board.GetNeighbor(Cell):
                if Board.board["opened"][Neighbor] == 0 and Board.board["pred_flags"][Neighbor] == 0:
                    A1.tiles_to_open.add(Neighbor)
        


class A2: #Some Logic Chains
    LogicChains = []
    Cell_LogicChains = {}
    new_LogicChains = []
    tiles_to_open = set([])
    no_of_revealed_tiles = 0
    no_of_pred_flags = 0
    def ResetLogicChains():
        A2.LogicChains = []
        A2.Cell_LogicChains = {}
        A2.new_LogicChains = []
        
    def A2():
        A2.tiles_to_open = set([])
        A2.no_of_revealed_tiles = 0
        A2.no_of_pred_flags = 0
        
        A2.ResetLogicChains()
        A2.GetLogicChains()
        A2.FindNewLogicChains()
        A2.ExecuteLogicChains()
        
        revealed_tiles = Open_tiles(A2.tiles_to_open)
        print(revealed_tiles)
        A2.no_of_revealed_tiles = len(revealed_tiles)
        
        print("Logic Chain, predicted " + str(A2.no_of_pred_flags) + " flags, revealed " + str(A2.no_of_revealed_tiles) + " tiles")
        return revealed_tiles
    
    def GetLogicChain(Cell):
        
        remaining_mines = Board.GetNumber(Cell) - Board.GetNoOfPredFlags(Cell)
        mine_candidates = set([])
        for Neighbor in Board.GetNeighbor(Cell):
            if Board.board["opened"][Neighbor] == 0 and Board.board["pred_flags"][Neighbor] == 0:
                mine_candidates.add(Neighbor)
        LogicChain = (mine_candidates,remaining_mines)
        return LogicChain
        

    def GetLogicChains():
        for Cell in Board.GetAdjopenedCells():
            LogicChain = A2.GetLogicChain(Cell)
            if len(LogicChain[0]) > 0:
                A2.LogicChains.append(LogicChain)
        
             
    def FindNewLogicChain(LC1,LC2): #LC = Logic Chain, mc = mine_candidates
        NewLCs = []

        mc1 = LC1[0]
        mc2 = LC2[0]

        no_candidates1 = len(mc1)
        no_candidates2 = len(mc2)
        no_mines1 = LC1[1]
        no_mines2 = LC2[1]
          
        diff1 = mc1.difference(mc2)
        diff2 = mc2.difference(mc1)
        
        symmetric_diff = mc1.symmetric_difference(mc2)
        no_mines_diff = abs(no_mines1 - no_mines2)
        union = mc1.union(mc2)
        intersection = mc1.intersection(mc2)

        criterion1 = len(symmetric_diff) > 0
        criterion2 = len(diff1) == no_mines1 - no_mines2
        criterion3 = len(diff2) == no_mines2 - no_mines1    

        if criterion1 and (criterion2 or criterion3):
            if no_mines1 == no_mines2: #Criterion 1
                mc3 = symmetric_diff
                no_mines3 = 0
                LC3 = (mc3,no_mines3)
                NewLCs.append(LC3)

            elif no_mines1 > no_mines2: #Criterion 2
                mc3 = diff1
                no_mines3 = no_mines_diff
                LC3 = (mc3,no_mines3)
                
                mc4 = diff2
                no_mines4 = 0
                LC4 = (mc4,no_mines4)
                
                if len(mc3) > 0:
                    NewLCs.append(LC3)
                if len(mc4) > 0:
                    NewLCs.append(LC4)

            elif no_mines1 < no_mines2: #Criterion 3
                mc3 = mc2.difference(mc1)
                no_mines3 = no_mines_diff
                LC3 = (mc3,no_mines3)
                
                mc4 = mc1.difference(mc2)
                no_mines4 = 0
                LC4 = (mc4,no_mines4)
                
                if len(mc3) > 0:
                    NewLCs.append(LC3)
                if len(mc4) > 0:
                    NewLCs.append(LC4)

        return NewLCs
    

    def FindNewLogicChains():

        for LogicChain1 in A2.LogicChains:
            for LogicChain2 in A2.LogicChains:
                NewLCs = A2.FindNewLogicChain(LogicChain1,LogicChain2)
                A2.new_LogicChains += NewLCs
                    
    
    def ExecuteLogicChain(LogicChain):
        mine_candidates = LogicChain[0]
        remaining_mines = LogicChain[1]
        if remaining_mines == 0:
            for Cell in mine_candidates:
                A2.tiles_to_open.add(Cell)
        elif remaining_mines == len(mine_candidates):
            for Cell in mine_candidates:
                A2.no_of_pred_flags +=1
                PredFlag_tile(Cell)
    
    def ExecuteLogicChains():
        for LogicChain in A2.LogicChains:
            A2.ExecuteLogicChain(LogicChain)
        for LogicChain in A2.new_LogicChains:
            A2.ExecuteLogicChain(LogicChain)
        
    def PrintLogicChains():
        LC_no = 0
        print("Old LC: ")
        for LC in A2.LogicChains:
            LC_no += 1
            print(LC_no,LC)

        print("New LC: ")
        for LC in A2.new_LogicChains:
            LC_no += 1
            print(LC_no,LC)



