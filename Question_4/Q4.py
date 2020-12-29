# -*- coding: utf-8 -*-
"""
Created on Dec 18 2020

Code for Qusetion 4

Please refer to the answer sheet to see a complete strategy explanation for
solving this question.

@author: Haolin Zhong
"""

def read_input(filename):
    """
    This function is used to read the input file and generate a corresponding matrix.
    """
    img= []
    with open(filename) as inputfile:
        img = inputfile.readlines()
        for i in range(0,len(img)):
            img[i] = img[i].rstrip("\n").split("\t")
            for j in range(0,len(img[i])):
                img[i][j] = int(img[i][j])
    return img


def label_img(img):
    """
    This function is used to label connected components in a given matrix.
    """
    row_range = len(img)
    col_range = len(img[0])
    
    # cur_label stores the current label
    global cur_label
    cur_label = 0
    
    # equal labels stores labels that are actually equal
    global equal_labels
    equal_labels = []
    
    # Traverse the matrix for the first time
    for i in range(0, row_range):
        for j in range(0, col_range):
            first_label_pos(i, j)
    
    # Integrate equal labels into equal label sets
    equal_label_sets = generate_equal_label_sets(equal_labels)
    
    # Traverse the matrix for the second time
    for i in range(0, row_range):
        for j in range(0, col_range):
            second_label_pos(i, j, equal_label_sets)
    
    return img

def first_label_pos(row, col):
    """
    The pixels in the image will be traversed from left to right, top to bottom.
    For every pixel, if it is equal to 0, move to next pixel, otherwise label it.
    """
    if img[row][col] == 0:
        return 0
    else:
        return check_neighbor(row, col)

def check_neighbor(row, col):
    """
    This function is used in the first traverse of the image. For a given
    position in the matrix, it will check the surronding position and give it a
    label, meanwhile stores labels into equal label sets.
    
    If the left pixel or the above pixel are not labeled, give the current pixel
    a new label.
    
    If one of the left pixel and the above pixel is labeled and the
    other one is not, or they are both given the same label, give the current
    pixel the same label.
    
    If the left pixel and the above pixel are labeled differently, give the
    current pixel the smaller label. The bigger label and the smaller label
    should actually be equal, so add the two labels in the corresponding list
    made up of equal labels.
    """
    global img
    global cur_label
    global equal_labels
    
    if row == 0 and col == 0:
        """
        As it is the first time we traverse the img and we are at the initial position,
        in the neighbor area there must be no labeled pixel. So we can directly give this
        pixel a new label.
        """
        cur_label += 1
        img[row][col] = cur_label
            
    elif row == 0 and col != 0:
        """
        As it is the first time we reach the last column at the first row,
        in the neighbor area only the left pixel may be labeled. So we only have to 
        check the left pixel.
        """
        left = img[row][col-1]
        if left != 0:
            img[row][col] = left
        else:
            cur_label += 1
            img[row][col] = cur_label
    
    elif row != 0 and col == 0:
        """
        If we are at the first column but not first row, in the neighbor area
        only the above pixel may be labeled. So we only have to check the above
        pixel.
        """
        up = img[row-1][col]
        if up != 0:
            img[row][col] = up
        else:
            cur_label += 1
            img[row][col] = cur_label
            
    elif row != 0 and col != 0:
        """
        If we are not at left or up margin of the img, check the left and above
        pixel.
        """
        left = img[row][col-1]
        up = img[row-1][col]
        if left == 0 and up == 0:
            cur_label += 1
            img[row][col] = cur_label
        elif left != 0 and up == 0:
            img[row][col] = left
        elif left == 0 and up != 0:
            img[row][col] = up
        elif left != 0 and up != 0:
            if left == up:
                img[row][col] = left
            else:
                true_label = min([left, up])
                # equal labels are stored into equal_labels in pair
                equal_labels.append([left,up])
                img[row][col] = true_label

            
def generate_equal_label_sets(raw_list):
    """
    Because equal labels are stored into equal_labels in pair, this function will
    integrate these pairs into several equal label sets. (It will integrate
    several lists which have shared elements into one list.)
    """
    for i in range(0,len(raw_list)):
        for j in range(0,len(raw_list)):
            if i == j:
                continue
            x = list(set(raw_list[i]+raw_list[j]))
            y = len(raw_list[i]) + len(raw_list[j])
            if len(x) < y:
                raw_list[i] = x
                raw_list[j] = [-1]
                
    equal_label_sets = []
    for equal_set in raw_list:
        if equal_set != [-1]:
            equal_label_sets.append(equal_set)
    return equal_label_sets

def second_label_pos(row, col, equal_label_sets):
    """
    This function is used in the second traverse of the image. For every pixel,
    if it is equal to 0, move to next pixel, otherwise re-label it according to
    it current label. For every current label, check which equal label set it
    is in, and re-label it with the smallest label in the set. After the 2nd
    traverse, all the connected components should be labeled correctly.
    """
    global img
    
    label = img[row][col]
    if label != 0:
        for i in equal_label_sets:
            if label in i:
                img[row][col] = min(i)
                
def re_label(img):
    """
    This function is used in the third traverse of the image. This traverse
    will make all the labels become continuous integers.
    """
    labels = []
    for i in range(0,len(img)):
        for j in range(0,len(img[0])):
            if img[i][j] != 0 and img[i][j] not in labels:
                labels.append(img[i][j])
    labels.sort()
    label_pairs = list(enumerate(labels, start = 1))
    
    for i in range(0,len(img)):
        for j in range(0,len(img[0])):
            for label_pair in label_pairs:
                if img[i][j] == label_pair[1]:
                    img[i][j] = label_pair[0]
                    
    return img

def output(labeled_img, outfilename):
    """
    This function is used to generate output file.
    """
    row_range = len(labeled_img)
    col_range = len(labeled_img[0])
    with open(outfilename, "w") as output:
        for i in range(0,row_range):
            for j in range(0,col_range):
                output.write(str(labeled_img[i][j])+" ")
            output.write("\n")

if __name__ == "__main__":
    img = read_input("input_question_4")
    labeled_img = label_img(img)
    re_labeled_img = re_label(labeled_img)
    output(re_labeled_img, "out_put_question_4")