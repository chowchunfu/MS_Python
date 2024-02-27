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

class imgs:
    imgs = {}
    storage = {}
    
    imgs["tile"] = GetImg("tile",board.GRID_SIZE)
    imgs["flag"] = GetImg("flag",board.GRID_SIZE)
    for num in range(0,9):
        filename = "num" + str(num)
        imgs[filename] = GetImg(filename,board.GRID_SIZE)

    
    