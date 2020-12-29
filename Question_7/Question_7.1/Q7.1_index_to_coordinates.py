# -*- coding: utf-8 -*-
"""
Created on Dec 21 2020

Code for Qusetion 7.1 （index to coordinate）

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
    coords = []
    for i in range(0,len(Is)):
        x2 = Is[i] // Ls[0]
        x1 = Is[i] % Ls[0]
        coords.append([x1,x2])
    return coords

def output(coords,filename):
    with open (filename, "w") as output:
        output.write("x1\tx2\n")
        for coord in coords:
            output.write(str(coord[0])+"\t"+str(coord[1])+"\n")

if __name__ == "__main__":
    Is = read_input("input_index_7_1.txt")
    coords = I_2_C(Is, [50,57])
    output(coords,"output_coordinates_7_1.txt")