# -*- coding: utf-8 -*-
"""
Created on Dec 18 2020

Code for Qusetion 5

Please refer to the answer sheet to see a complete strategy explanation for
solving this question.

@author: Haolin Zhong
"""

"""
    Strategy for choose beads:
    
    The ideal way should be (no penalty):
        1. Choose the bead whose color is different with beads at left and above;
        2. The number of the chosen bead must over 0;
        3. We preferentially put the kind of beads with the biggest number;
    
    If we cannot choose in the ideal way, the second way should be (1 pts penalty for place one bead):
        1. Choose the bead whose color is different with beads at left or above;
        2. The number of the chosen bead must over 0;
        3. We preferentially put the kind of beads with the biggest number;
        
    If we cannot even choose in the second way, the third way should be (2 pts penalty for place one bead):
        1. Choose the bead whose color is the same as beads at left and above;
        2. The number of the chosen bead must over 0;
        3. We preferentially put the kind of beads with the biggest number;
        
"""

def choose_color_without_penalty(left, above, bead_nums, prior_color):
    """
    This function will place a bead of a certain color on the given postion
    according to the colors of beads at the left and the above.
    
    left: the color of the bead at the left postion of the given postion
    above: the color of the bead at the above postion of the given postion
    bead_nums: a list containing all the numbers of beads in different colors
    prior_color: the index of the color that the kind of beads with the biggest number belong to
    """
    cur_bead_num = 0
    cur_bead_color = -1
    
    
    """
    At the first row, first column, there are no bead at the left or the above position.
    So, we should directly put the kind of beads with the biggest number
    """
    if left == -1 and above == -1:
        return prior_color
    
    
    # For other positions:
    # the ideal way
    for i in range(0, len(bead_nums)):
        if i!=left and i!= above and bead_nums[i] > 0:
            # find the kind of beads with the biggest number, put it on the given positon
            if bead_nums[i] > cur_bead_num:
                cur_bead_num = bead_nums[i]
                cur_bead_color = i
    
    """
    If we find a suitable color in the ideal way, this function will return the index of the color
    Otherwise cur_bead_color will remain equals to -1, and lead to using another function,
    choose_color_with_penalty, to choose bead.
    """
    return cur_bead_color


def choose_color_with_penalty(left, above, bead_nums):
    cur_bead_color = -1
    cur_bead_num = 0
    
    """
    If the beads at the left and the above have different colors,
    we should directly choose the kind of beads with the biggest number,
    we will either get the color of the left or the color of the above
    and receive a penalty of 1.
    """
    if left != above:
        for i in range(0,len(bead_nums)):
            if bead_nums[i] > cur_bead_num:
                cur_bead_num = bead_nums[i]
                cur_bead_color = i
        return cur_bead_color
    # If the beads at the left and the above have the same color,
    # we can only choose the bead with the same color
    elif left == above:
        return left

def coloring(L, color_names, bead_nums, output_name):
    """
    For given L by L square and different numbers and colors of beads, this 
    function will output a file depicting the optimized arrangement of beads
    with least penalty.
    
    color_names: a list containing all the abbreviations of colors of beads.
    bead_nums: a list containing all the numbers of beads in different colors.
    (The two lists should have corresponding orders.)
    
    """
    grid = []
    # The variable, left, stores the index of color of the left position of a given position in the grid
    left = -1
    # We should always put the color that most beads belong to in the first row and first column
    prior_color = bead_nums.index(max(bead_nums))
    penalty = 0
    
    for i in range(0,L):
        # cur_line was used to store the arrangement of beads in the line i, i.e. grid[i]
        cur_line = []
        # cur_bead was used to store the index of the bead which should be placed in the given postion, i.e. grid[i][j]
        cur_bead = 0
        left = -1
        for j in range(0,L):
            # for the first line, there are no above line
            if i == 0:
                cur_bead = choose_color_without_penalty(left, -1, bead_nums, prior_color)
                if cur_bead == -1:
                    cur_bead = choose_color_with_penalty(left, -1, bead_nums)
                    """
                    for the first line we only have to consider whether the current bead is the same
                    as the left bead.
                    """
                    if cur_bead == left:
                        penalty += 1
                    
                cur_line.append(cur_bead)     # place the bead
                bead_nums[cur_bead] -= 1      # reduce the number of the placed bead
                left = cur_bead               # move to next position
            
            # for other lines:
            else:
                cur_bead = choose_color_without_penalty(left, grid[i-1][j], bead_nums, prior_color)
                if cur_bead == -1:
                    cur_bead = choose_color_with_penalty(left, grid[i-1][j], bead_nums)
                    if cur_bead == left:
                        penalty += 1
                    if cur_bead == grid[i-1][j]:
                        penalty += 1
                cur_line.append(cur_bead)
                bead_nums[cur_bead] -= 1
                left = cur_bead
        # Now we have completed filling the current line. Store the line into grid.
        grid.append(cur_line)
    
    print(penalty)
    with open(output_name,"w") as output:
        for i in range(0,L):
            for j in range(0,L):
                output.write(str(color_names[grid[i][j]])+" ")
            output.write("\n")

if __name__ == "__main__":
    coloring(5, ["R","B"], [12,13], "output_question_5_1")
    coloring(64, ["R","B","G","W","Y"], [139, 1451, 977, 1072, 457], "output_question_5_2")