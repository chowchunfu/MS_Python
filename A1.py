# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:05:15 2024

@author: someone
"""

from Board import *

class Alg:
    A0 = 1



class A0: #First corner and Random guess
    tile_to_open = (0,0)
    
    def first_move(): #First corner move
        firstCell = (0,0)
        Board.CheckFirstClick(firstCell)
        revealed_tile = Open_tile(firstCell)
        print("First Move " + str(firstCell) + ",Revealed " + str(revealed_tile))
        return revealed_tile
        
    
    def random_move(): #Random guess
        candidates = Board.GetPotentiallysafeCells()
        no_of_candidates = len(candidates)
        randomCell = candidates[int(random.random() * no_of_candidates)]
        A0.tile_to_open = randomCell
        revealed_tile = Open_tile(randomCell)
        print("Random Move " + str(randomCell) + ",Revealed " + str(revealed_tile))
        return revealed_tile

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
        
    def detect_flag(Cell):
        satisfaction = 0
        satisfaction += Board.GetNumber(Cell)
        for Neighbor in Board.GetNeighbor(Cell):
            satisfaction += Board.board["opened"][Neighbor]
        
        req_satisfaction = len(Board.GetNeighbor(Cell))
        if satisfaction == req_satisfaction:
            for Neighbor in Board.GetNeighbor(Cell):
                if Board.board["opened"][Neighbor] == 0 and Board.board["pred_flags"][Neighbor] == 0:
                    Board.board["pred_flags"][Neighbor] = 1
                    A1.no_of_pred_flags += 1


    def chording(Cell):
        no_of_neighbor_flags = 0
        for Neighbor in Board.GetNeighbor(Cell):
            no_of_neighbor_flags += Board.board["pred_flags"][Neighbor]
        
        if Board.GetNumber(Cell) == no_of_neighbor_flags:
            for Neighbor in Board.GetNeighbor(Cell):
                if Board.board["opened"][Neighbor] == 0 and Board.board["pred_flags"][Neighbor] == 0:
                    A1.tiles_to_open.add(Neighbor)
        
