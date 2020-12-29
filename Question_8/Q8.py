# -*- coding: utf-8 -*-
"""
Created on Dec 24 2020

Code for Qusetion 8

Please refer to the answer sheet to see a complete strategy explanation for
solving this question.

@author: Haolin Zhong
"""

import matplotlib.pyplot as plt

def Solve_Equation(t):

    global k1
    global k2
    global k3
    
    # we use um/s to calculate
    k1 = 100/60
    k2 = 600/60
    k3 = 150/60
    
    # initial concentration
    C_0 = {"E": [1], "S": [10], "ES": [0], "P": [0]}
    C = C_0
    
    h = 0.01
    # because stepwise h = 0.01s, to get the concentration at t, 100t steps should be performed
    N = int(100*t)
    
    # record the initial V_{P} and C_{S} for 8.3
    V_P = [0]
    C_S = [10]
    
    # perform Runge Kutta method for N times
    for i in range(0,N):
        C = Fourth_order_Runge_Kutta(h,C)
        # record for 8.3
        V_P.append(k3*C["ES"][0])
        C_S.append(C["S"][0])
    
    # calculate rate of changes based on concentration at time t
    R = {}
    R["E"] = -k1*C["E"][0]*C["S"][0] + (k2+k3)*C["ES"][0]
    R["S"] = -k1*C["E"][0]*C["S"][0] + k2*C["ES"][0]
    R["ES"] = k1*C["E"][0]*C["S"][0] - (k2+k3)*C["ES"][0]
    R["P"] = k3*C["ES"][0]
        
    return R, C, V_P, C_S

def Fourth_order_Runge_Kutta(h, C):
    global k1
    global k2
    global k3

    cur_K = {"E": [], "S": [], "ES": [], "P": []}
    cur_C = C
    
    # calculate K1
    calc_K(1, cur_K, cur_C)
    # calculate c + h/2*k1
    update_C(1, 0.5, h, cur_K, cur_C)
    # calculate K2
    calc_K(2, cur_K, cur_C)
    # calculate c + h/2*k2
    update_C(2, 0.5, h, cur_K, cur_C)
    # calculate K3
    calc_K(3, cur_K, cur_C)
    # calculate c + h*k3
    update_C(3, 1, h, cur_K, cur_C)
    # calculate K4
    calc_K(4, cur_K, cur_C)
    
    all_species = ["E", "S", "ES", "P"]
    C_new = {}
    # calculate c_{n+1} = c_{n} + h/6 * (K1 + 2K2 + 2K3 + K4)
    for species in all_species:
        C_new[species] = [max(0,cur_C[species][0] + h*(cur_K[species][0]+2*cur_K[species][1]+2*cur_K[species][2]+cur_K[species][3])/6)]
    
    # return the concentration after h
    return C_new

def calc_K(i, cur_K, cur_C):
    # calculate K by C 
    global k1
    global k2
    global k3
    cur_K["E"].append(-k1*cur_C["E"][i-1]*cur_C["S"][i-1] + (k2+k3)*cur_C["ES"][i-1])
    cur_K["S"].append(-k1*cur_C["E"][i-1]*cur_C["S"][i-1] + k2*cur_C["ES"][i-1])
    cur_K["ES"].append(k1*cur_C["E"][i-1]*cur_C["S"][i-1] - (k2+k3)*cur_C["ES"][i-1])
    cur_K["P"].append(k3*cur_C["ES"][i-1])
    
def update_C(i, a, h, cur_K, cur_C):
    # calculate C + a/h * K_{n}
    cur_C["E"].append(max(0,cur_C["E"][0] + a*h*cur_K["E"][i-1]))
    cur_C["S"].append(max(0,cur_C["S"][0] + a*h*cur_K["S"][i-1]))
    cur_C["ES"].append(max(0,cur_C["ES"][0] + a*h*cur_K["ES"][i-1]))
    cur_C["P"].append(max(0,cur_C["P"][0] + a*h*cur_K["P"][i-1]))     


if __name__ == "__main__":
    # 200s
    _, _, V_P, C_S = Solve_Equation(200)
    
    plt.rcParams['figure.dpi'] = 200
    plt.plot(C_S, V_P)
    plt.xlim(0, 10)
    plt.ylim(0, 1.4)
    plt.xlabel("${C_s}$ ($\mu$M)")
    plt.ylabel("$V$ ($\mu$M/s)")
    plt.title("$V$-${C_s}$ Plot")
    plt.show()
