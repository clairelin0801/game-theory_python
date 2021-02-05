# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 01:10:21 2021

@author: claire
"""
import nashpy as nash
import numpy as np

# 建立遊戲一__ payoff matrix
A = np.array([[1,0],[3,1]])
B = np.array([[3,1],[1,0]])
game1 = nash.Game(A,B)
game1
# Find the Nash Equilibrium with Support Enumeration"
equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)


# 建立遊戲二__ payoff matrix
A = np.array([[3,0],[0,1]])
B = np.array([[1,0],[0,3]])
game2 = nash.Game(A,B)
game2
# Find the Nash Equilibrium with Support Enumeration
equilibria = game2.support_enumeration()
for eq in equilibria:
    print(eq)

# Calculate Utilities
sigma_r = np.array([.75,.25])
sigma_c = np.array([.25,.75])
pd = nash.Game(A, B)
pd[sigma_r, sigma_c]

u_r = 0.75*0.25*3 + 0.75*0.25*0 + 0.75*0.25*0 + 0.75*0.25*1
u_c = 0.25*0.75*0 + 0.75*0.25*0 + 0.75*0.25*1 + 0.75*0.25*3
print(u_r,u_c)  #r:row,c:column

# Create the payoff matrix
甲 = np.array([[-3,1],[-5,-2]])
乙 = np.array([[-3,-1],[-5,-2]]) 
game4 = nash.Game(甲,乙)
game4
# Find the Nash Equilibrium with Support Enumeration
equilibria = game4.support_enumeration()
for eq in equilibria:
    print(eq)
