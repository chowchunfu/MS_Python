# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:10:49 2024

@author: someone
"""


LC1 = ({(12, 0), (12, 1), (12,2)}, 1)
LC2 = ({(12, 1), (12,2)}, 1)

LC3 = ({(25, 3), (25, 5), (26, 3), (27, 3), (25, 4)}, 2)
LC4 = ({(27, 3), (28, 3), (26, 3)}, 1)
LC5 = ({(25, 3), (25, 5), (26, 3), (27, 3), (25, 4)}, 4)

def FindNewLogicChain(LC1,LC2): #LC = Logic Chain, mc = mine_candidates
    NewLCs = []

    mc1 = LC1[0]
    mc2 = LC2[0]

    no_candidates1 = len(mc1)
    no_candidates2 = len(mc2)
    remaining_mines1 = LC1[1]
    remaining_mines2 = LC2[1]
      
    diff1 = mc1.difference(mc2)
    diff2 = mc2.difference(mc1)
    print(diff1)
    
    symmetric_diff = mc1.symmetric_difference(mc2)
    remaining_mines_diff = abs(remaining_mines1 - remaining_mines2)
    union = mc1.union(mc2)
    intersection = mc1.intersection(mc2)

    criterion1 = len(symmetric_diff) > 0
    criterion2 = len(diff1) == remaining_mines1 - remaining_mines2
    criterion3 = len(diff2) == remaining_mines2 - remaining_mines1

    print(criterion1, criterion2, criterion3)
    

    if criterion1 and (criterion2 or criterion3):
        if remaining_mines1 == remaining_mines2: #Criterion 1
            mc3 = symmetric_diff
            remaining_mines3 = 0
            LC3 = (mc3,remaining_mines3)
            NewLCs.append(LC3)
            print("C1")
        elif remaining_mines1 > remaining_mines2: #Criterion 2
            mc3 = diff1
            remaining_mines3 = remaining_mines_diff
            LC3 = (mc3,remaining_mines3)
            
            mc4 = diff2
            remaining_mines4 = 0
            LC4 = (mc4,remaining_mines4)
            
            if len(mc3) > 0:
                NewLCs.append(LC3)
            if len(mc4) > 0:
                NewLCs.append(LC4)
            print("C2")
        elif remaining_mines1 < remaining_mines2: #Criterion 3
            mc3 = mc2.difference(mc1)
            remaining_mines3 = remaining_mines_diff
            LC3 = (mc3,remaining_mines3)
            
            mc4 = mc1.difference(mc2)
            remaining_mines4 = 0
            LC4 = (mc4,remaining_mines4)
            
            if len(mc3) > 0:
                NewLCs.append(LC3)
            if len(mc4) > 0:
                NewLCs.append(LC4)
            print("C3")
    return NewLCs
print(FindNewLogicChain(LC1,LC2))
print(FindNewLogicChain(LC3,LC4))
print(FindNewLogicChain(LC5,LC4))
