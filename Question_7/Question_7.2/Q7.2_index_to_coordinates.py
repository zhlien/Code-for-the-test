# -*- coding: utf-8 -*-
"""
Created on Dec 21 2020

Code for Qusetion 7.2 （index to coordinate）

Please refer to the answer sheet to see a complete strategy explanation for
solving this question.

@author: Haolin Zhong
"""

def read_input(filename):
    with open(filename) as input_data:
        Is = input_data.readlines()[1:]
        for i in range(0,len(Is)):
            Is[i] = int(Is[i].rstrip("\n"))
    return Is

def I_2_C(Is, Ls):
    coef = [1]
    cur_coef = 1
    for i in range(0,len(Ls)-1):
        cur_coef = Ls[i]*cur_coef
        coef.append(cur_coef)
    coef.reverse()
    
    coords = []
    for i in range(0,len(Is)):
        cur_I = Is[i]
        cur_coord = []
        for j in range(0,len(Ls)):
            x = cur_I // coef[j]
            cur_I = cur_I % coef[j]
            cur_coord.append(x)
        cur_coord.reverse()
        coords.append(cur_coord)
    return coords

def output(coords,filename):
    with open (filename, "w") as output:
        output.write("x1\tx2\tx3\tx4\tx5\tx6\n")
        for coord in coords:
            for i in range(0,len(coord)):
                if i != 5:
                    output.write(str(coord[i])+"\t")
                else:
                    output.write(str(coord[i])+"\n")

if __name__ == "__main__":
    Is = read_input("input_index_7_2.txt")
    coords = I_2_C(Is, [4,8,5,9,6,7])
    output(coords,"output_coordinates_7_2.txt")