# -*- coding: utf-8 -*-
"""
Created on Dec 21 2020

Code for Qusetion 7.1 （coordinate to index）

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
            coords[i][0] = int(coords[i][0])
            coords[i][1] = int(coords[i][1])
    return coords

def C_2_I(coords, Ls):
    Is = []
    for i in range(0,len(coords)):
        Is.append(coords[i][0] + Ls[0] * coords[i][1])
    return Is

def output(Is,filename):
    with open (filename, "w") as output:
        output.write("index\n")
        for I in Is:
            output.write(str(I)+"\n")

if __name__ == "__main__":
    coords = read_input("input_coordinates_7_1.txt")
    Is = C_2_I(coords, [50,57])
    output(Is,"output_index_7_1.txt")