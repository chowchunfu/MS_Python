# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:14:22 2024

@author: someone
"""
import random

WINRATE = 0.41
REQ_CONSECUTIVE_GAMES = 100
REQ_WINS = 53

def IsGameWin(WINRATE):
    rng = random.random()
    Iswin = rng < WINRATE
    if Iswin:
        return 1
    else:
        return 0
    


def GetGamesToMastery(REQ_CONSECUTIVE_GAMES,REQ_WINS):
    game_log = {}
    games = 0
    playing = True
    while playing:
        games += 1
        game_log[games] = IsGameWin(WINRATE)
        
        if games < REQ_CONSECUTIVE_GAMES:
            current_consecutive_games = games
        else:
            current_consecutive_games = REQ_CONSECUTIVE_GAMES
            
        wins = 0
        for past_game in range(games-current_consecutive_games+1,games+1):
            wins += game_log[past_game]
        
        playing = (wins < REQ_WINS)

    return games

file = open("Mastery.csv","w")

for i in range(500):
    games_to_mastery = GetGamesToMastery(REQ_CONSECUTIVE_GAMES,REQ_WINS)
    file.writelines(str(games_to_mastery) + "\n")
    print(games_to_mastery)
    
file.close()



