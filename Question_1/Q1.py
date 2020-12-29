# -*- coding: utf-8 -*-
"""
Created on Dec 17 2020

Code for Qusetion 1

Please refer to the answer sheet to see a complete strategy explanation for
solving this question.

@author: Haolin Zhong
"""

def get_path(m, n, s):
    """
    We will use this function to find one operation in a m*n matrix 
    for a given summed number s.
    """
    """
    Obviously, numbers after D moves plus the initial 1 should summed up to 
    m(m+1)/2, i.e. 1+2+3+...+m.Therefore, sum of numbers after R moves, named 
    S_R, should be S - m(m+1)/2. And there are n - 1 R moves in total.
    """
    s_R = s - 1/2*m*(m+1)
    
    """
    Considering the extreme cases will tell us the range of s_R. If the s_R 
    calculated based on the given s is out of the range, there will be no operation
    can result in the given s.
    If all the right moves are performed at row 1, we will get the minimum s_R.
    If all the right moves are performed at row m, we will get the maximum s_R.
    """
    min_s_R = 1 * (n-1)
    max_s_R = m * (n-1)
    
    # Set the range of s_R
    if s_R < min_s_R or s_R > max_s_R:
        return("Error: no path can generate the given value in the given matrix.")
    
    else:
        """
        We can firstly calculate S_R floor divided by n-1 and get a integer avg_row,
        and the remainder res. If we put all the R moves on the row whose index
        is avg_row, the summed up number should be S_R - res. If res is larger 
        than 0, to make all the R moves summed up to S_R, we should eliminate 
        by moving some R moves in avg row.
        """
        avg_row = s_R // (n-1)
        res = s_R % (n-1)
        
        
        """
        Moving one R move from avg row to row m will reduce res by m - avg_row.
        After moving some R to row m, we may need to move another one R to a row
        between avg row and row m to eliminate the final res.
        """
        cpst = m - avg_row
        
        # num_row_m stores how much R should be moved to row m
        num_row_m = 0
        # cp_row stores which row an R should be moved to for eliminating the final res
        cp_row = 0
        
        
        if res >= cpst:
            """
            If res is larger than cpst, then We need move R to row_m to 
            eliminate the res.
            """
            # Move as more R as possible to eliminate res
            num_row_m = res//cpst
            # Move one R to cp_row to eliminate the final res
            cp_row = avg_row + res % cpst
            # store how many R were actually put on the avg row
            num_avg_row = n-2-num_row_m
        
        elif res > 0:
            """
            If res is larger than 0 but smaller than cpst, then we only need 
            moving one R to a row between avg row and row m to eliminate res.
            """
            # Move one R to cp_row to eliminate the final res
            cp_row = avg_row + res
            # store how many R were actually put on the avg row
            num_avg_row = n-2
        
            
        else:
            """
            If res = 0, we can directly put all the R on avg row.
            """
            # No need for moving R
            cp_row = 0
            # store how many R were actually put on the avg row
            num_avg_row = n-1
        
        path_str = ""
        # Put a number of D moves to arrive avg row
        path_str += "D"*int(avg_row-1)
        # Put R on avg row
        path_str += "R"*int(num_avg_row)
        
        # If one R was moved to cp_row
        if cp_row >0:
            # Put a number of D moves to arrive cp row
            path_str += "D"*int(cp_row-avg_row)
            # Put one R on cp row
            path_str += "R"
            # Put a number of D moves to arrive row m
            path_str += "D"*int(m-cp_row)
            # Put R on row m
            path_str += "R"*int(num_row_m)
        else:
            # Put a number of D moves to arrive row m
            path_str += "D"*int(m-avg_row)
            # Put R on row m
            path_str += "R"*int(num_row_m)
        return(path_str)

if __name__ == "__main__":
    with open("output_question_1", "w") as output:
        output.write("65\t" + str(get_path(9,9,65)) + "\n")
        output.write("72\t" + str(get_path(9,9,72)) + "\n")
        output.write("90\t" + str(get_path(9,9,90)) + "\n")
        output.write("110\t" + str(get_path(9,9,110)) + "\n")
        output.write("\n")
        output.write("87127231192\t" + str(get_path(90000,100000,87127231192)) + "\n")
        output.write("5994891682\t" + str(get_path(90000,100000,5994891682)))