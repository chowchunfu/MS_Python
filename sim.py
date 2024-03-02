# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:05:15 2024

@author: someone
"""

from Board import *
from A1 import *

class sim:
    wins = 0
    loses = 0
    games = 0
    playing = True
    
    def trigger_game_lose():
        sim.loses += 1
        sim.games += 1
        sim.playing = False
        print("L")
        sim.report_game_stat()
        
    def trigger_game_win():
        sim.wins += 1
        sim.games += 1
        sim.playing = False
        print("W")
        sim.report_game_stat()
        
    def reset_game_stat():
        sim.wins = 0
        sim.loses = 0
        sim.games = 0
    
    def report_game_stat():
        print("Games: " + str(sim.games) + ", Wins: " + str(sim.wins) + ", Loses: " + str(sim.loses))
        
    def sim(games,Alg_level):
        sim.reset_game_stat
        for game in range(games):
            Board.ResetBoard_Rd()
            sim.playing = True
            print(GetBoardString())
            sim.Check_GameState(A0.first_move())
            
            sim.play(Alg_level)
            
            
    
    def Check_GameState(revealed_tile):
        if revealed_tile == "*":
            sim.trigger_game_lose()
        elif Board.opened_current == Board.opened_max:
            sim.trigger_game_win()
    
    def Check_GameStates(revealed_tiles):
        if "*" in revealed_tiles:
            sim.trigger_game_lose()
        elif Board.opened_current == Board.opened_max:
            sim.trigger_game_win()
    
    def play(Alg_level):
        if Alg_level == "0" or Alg_level == "A0":
            sim.play_as_A0()
        elif Alg_level == "1" or Alg_level == "A1":
            sim.play_as_A1()
        elif Alg_level == "2" or Alg_level == "A2":
            sim.play_as_A2()

    
    
    def play_as_A0():
        while sim.playing:
            sim.Check_GameStates(A0.A0())
            if A0.no_of_revealed_tiles == 0:
                sim.Check_GameState(A0.random_move())
            

    def play_as_A1():
        print(GetBoardString())
        while sim.playing:
            sim.Check_GameStates(A1.A1())
        
            if A1.no_of_revealed_tiles == 0:
                sim.Check_GameState(A0.random_move())
    
    def play_as_A2():
        while sim.playing:
            Alg_level = "A1"
            sim.Check_GameStates(A1.A1())
            
            if A1.no_of_revealed_tiles == 0:
                Alg_level = "A2"
            if Alg_level == "A2":
                sim.Check_GameStates(A2.A2())
                if A2.no_of_revealed_tiles == 0:
                    sim.Check_GameState(A0.random_move())
    
        
sim.sim(25000,"A2")






