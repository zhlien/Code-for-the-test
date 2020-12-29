# -*- coding: utf-8 -*-
"""
Created on Dec 20 2020

Code for Qusetion 6

Please refer to the answer sheet to see a complete strategy explanation for
solving this question.

@author: Haolin Zhong
"""

def get_polygon(filename):
    """
    This function is used to read the input file and generate a list containing
    all the vertexs of the polygon.
    """
    polygon = []
    with open(filename) as input:
        for line in input:
            if line:
                vertex = line.rstrip("\n")
                vertex = vertex.split(" ")
                vertex[0] = int(vertex[0])
                vertex[1] = int(vertex[1])
                polygon.append(vertex)
    # append the first vertex will bring convenience when traverse every edge 
    polygon.append(polygon[0])
    return polygon

def get_points(filename):
    """
    This function is used to read the input file and generate a list containing
    all the points whose position are to be determined.
    """
    points = []
    with open(filename) as input:
        for line in input:
            line = line.rstrip("\n")
            if line:
                point = line.split(" ")
                point[0] = int(point[0])
                point[1] = int(point[1])
                points.append(point)
    return points


def check_intersect_by_y(p1, p2, p):
    """
    We will release a ray y=p_{y} from point p and see the intersect condition
    between the ray and the line defined by p1 and p2.
    """
    
    # We can only expect to get a intersect point when p_{x} is between p1_{x} and p2{x}
    cond = ((min(p1[0], p2[0]) <= p[0]) and (p[0] <= max(p1[0], p2[0])))
    
    """
    If the ray from the point is coincide with an edge of the polygon, no 
    intersect point will be counted from this edge.
    """
    if p1[0] == p2[0]:
        return 0
    
    else:
        if cond:
            k = (p1[1]-p2[1])/(p1[0]-p2[0])
            b = p1[1] - k * p1[0]
            intersect_y = k * p[0] + b
            
            """
            （1）When counting the intersect points, the relative position between 
            the ray and every edge was checked one by one. If the intersect 
            point happens to be one of the vertices of an edge, it will be 
            counted twice and results in error. So, to fix this error, when the
            intersect point locates at the second vertex of an edge, it will not
            be counted. (Vertices are arranged in clockwise order)
            """
            
            """
            （2）To avoid the situation that the points is located at one edge of the
            polygon, the coordinate of intersect point was compared with the point.
            If they share the same coordinate then the point will be directly 
            determined to be inside the polygon.
            """
            # (1)
            if abs(intersect_y - p2[1]) < 10**(-9):
                return 0
            # (2)
            elif abs(intersect_y - p[1]) < 10**(-9):
                return "Inside"
            
            elif intersect_y > p[1]:
                return 1
        
            elif intersect_y < p[1]:
                return 0
        else:
            return 0

def check_intersect_by_x(p1, p2, p):
    """
    We will release a ray x=p_{x} from point p and see the intersect condition
    between the ray and the line defined by p1 and p2. The second ray is used to
    aviod the situation that the first ray is tangent to the polygon.
    """
    # We can only expect to get a intersect point when p_{y} is between p1_{y} and p2{y}
    cond = ((min(p1[1], p2[1]) <= p[1]) and (p[1] <= max(p1[1], p2[1])))
    
    """
    If the ray from the point is coincide with an edge of the polygon, no 
    intersect point will be counted from this edge.
    """
    if p1[1] == p2[1]:
        return 0
    
    else:
        if cond:
            k = (p1[0]-p2[0])/(p1[1]-p2[1])
            b = p1[0] - k * p1[1]
            intersect_x = k * p[1] + b
            
            # (1)
            if abs(intersect_x - p2[0]) < 10**(-9):
                return 0
            # (2)
            elif abs(intersect_x - p[0]) < 10**(-9):
                return "Inside"
            
            elif intersect_x > p[0]:
                return 1
        
            elif intersect_x < p[0]:
                return 0
        else:
            return 0

if __name__ == "__main__":
    polygon = get_polygon("input_question_6_polygon")
    points = get_points("input_question_6_points")
    point_cond = []
    for i in range(0,len(points)):
        intersect_cond_y = []
        intersect_cond_x = []
        for j in range(0,len(polygon)-1):
            intersect_cond_y.append(check_intersect_by_y(polygon[j], polygon[j+1], points[i]))
            intersect_cond_x.append(check_intersect_by_x(polygon[j], polygon[j+1], points[i]))
        
        # If the point happens to on the edge of the polygon:
        if ("Inside" in intersect_cond_y) or ("Inside" in intersect_cond_x):
            point_cond.append("Inside")
        else:
            total_intersect_y = sum(intersect_cond_y)
            total_intersect_x = sum(intersect_cond_x)
            # When the two ray both lead to odd number of intersect point, the point should be inside the polygon
            if (total_intersect_y % 2) == 1 and (total_intersect_x % 2 == 1):
                point_cond.append("Inside")
            else:
                point_cond.append("Outside")
    
    with open("output_question_6","w") as output:
        output.write("Point\tState\n")
        for i in range(0,len(points)):
            output.write(str(tuple(points[i]))+"\t"+str(point_cond[i])+"\n")
