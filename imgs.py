# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:57:09 2024

@author: someone
"""

import tkinter as tk
from PIL import ImageTk, Image
from Board import *

def GetImg(filename,GRID_SIZE):
    img = Image.open("imgs\\" + filename + ".png").resize((GRID_SIZE,GRID_SIZE))
    img = ImageTk.PhotoImage(img)
    return img

def NewImg(GRIDSIZE,color):
    img = Image.new("RGBA",(GRIDSIZE,GRIDSIZE),color)
    img = ImageTk.PhotoImage(img)
    return img

class imgs:
    imgs = {}
    storage = {}
    
    imgs["tile"] = GetImg("tile",Board.GRID_SIZE)
    imgs["flag"] = GetImg("flag",Board.GRID_SIZE)
    for num in range(0,9):
        filename = "num" + str(num)
        imgs[filename] = GetImg(filename,Board.GRID_SIZE)

    imgs["green_tile"] = NewImg(Board.GRID_SIZE,(0,255,0,96))
    imgs["blue_tile"] = NewImg(Board.GRID_SIZE,(0,0,255,96))
    imgs["yellow_tile"] = NewImg(Board.GRID_SIZE,(255,255,0,96))
    imgs["red_tile"] = NewImg(Board.GRID_SIZE,(255,0,0,96))
    imgs["magenta_tile"] = NewImg(Board.GRID_SIZE,(255,0,255,96))
    imgs["white_tile"] = NewImg(Board.GRID_SIZE,(255,255,255,96))
    
    for filename in imgs.keys():
        storage[filename] = {}