# -*- coding: utf-8 -*-
"""
Created on Dec 21 2020

Code for Qusetion 7.2 （coordinate to index）

Please refer to the answer sheet to see a complete strategy explanation for
solving this question.

@author: Haolin Zhong
"""

def read_input(filename):
    with open(filename) as input_data:
        coords = input_data.readlines()[1:]
        for i in range(0,len(coords)):
            coords[i] = coords[i].rstrip("\n")
            coords[i] = coords[i].split("\t")
            for j in range(0,len(coords[i])):
                coords[i][j] = int(coords[i][j])
    return coords

def C_2_I(coords, Ls):
    coef = [1]
    cur_coef = 1
    for i in range(0,len(Ls)-1):
        cur_coef = Ls[i]*cur_coef
        coef.append(cur_coef)
    
    Is = []
    for i in range(0,len(coords)):
        cur_I = 0
        for j in range(0, len(coords[i])):
            cur_I += coords[i][j] * coef[j]
        Is.append(cur_I)
    return Is

def output(Is,filename):
    with open (filename, "w") as output:
        output.write("index\n")
        for I in Is:
            output.write(str(I)+"\n")
            
if __name__ == "__main__":
    coords = read_input("input_coordinates_7_2.txt")
    Is = C_2_I(coords, [4,8,5,9,6,7])
    output(Is,"output_index_7_2.txt")