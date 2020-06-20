#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:08:41 2020

@author: Vaishakh
"""

import math
from d3g.vector import magnitude,dotProduct

def lines(line1 = [[0,0,0],[1,1,1]],line2 = [[0,0,0],[2,2,2]]):
    """
    

    Parameters
    ----------
    line1 : TYPE-> list of 2 sublists
        DESCRIPTION-> The list of 2 sublists where first sublist is a 
        list of coordinates of the point line passing through and second 
        sublist is a list of direction ratios of the line.
        The default is [[0,0,0],[1,1,1]].
    line2 : TYPE-> list of 2 sublists
        DESCRIPTION-> The list of 2 sublists where first sublist is a 
        list of coordinates of the point line passing through and second 
        sublist is a list of direction ratios of the line.
        The default is [[0,0,0],[1,1,1]].

    Returns
    -------
    result : TYPE-> degree
        DESCRIPTION-> Angle between two lines.
        
    Example:
        Find the angle between the lines,
                x + 3 = y - 5 = z + 6
        line1: ------  ------  ------ 
                  2       4       2
        
                x - 5 = y + 4 = z + 7
        line2: ------  ------  ------ 
                  3       5       1
                  
        Formula:
           cos θ =  | b1 . b2 |
                   ______________
                    | b1 || b2 |
        
	>>from d3g.angle import lines
        >>lines(line1 = [ [-3, 5, -6], [2, 4, 2] ], line2 = [ [5, -4, -7], [3, 5, 1] ])
        14.963217433307127
        
    """
    numerator=abs(dotProduct(line1[1], line2[1]))
    denominator=magnitude(line1[1])*magnitude(line2[1])
    result=numerator/denominator
    result=180*math.acos(result)/math.pi
    return result

def planes(plane1 = [1, 1, 1, 1], plane2 = [1, 2, 3, 4]):
    """
    

    Parameters
    ----------
    plane1 : TYPE-> list
        DESCRIPTION -> list of 3 direction ratios of the normal of 
        the plane and the intercept. 
        The default is [1, 1, 1, 1].
    plane2 : TYPE-> list
        DESCRIPTION -> list of 3 direction ratios of the normal of 
        the plane and the intercept. 
        The default is [1, 2, 3, 4]..

    Returns
    -------
    result : TYPE-> degree
        DESCRIPTION-> Angle between two planes.
        
    Example:
        Find the angle between the planes,
        plane1: x + y + z = 1
        plane2: x + 2y + 3z = 4
                  
        Formula:
           cos θ =  | n1 . n2 |
                   ______________
                    | n1 || n2 |
                    
	>>from d3g.angle import planes
        >>planes(plane1 = [1, 1, 1, 1], plane2 = [1, 2, 3, 4])
        22.207654298596495

    """
    
    plane1=plane1[:-1]
    plane2=plane2[:-1]
    numerator=abs(dotProduct(plane1, plane2))
    denominator=magnitude(plane1)*magnitude(plane2)
    result=numerator/denominator
    result=180*math.acos(result)/math.pi
    return result

def lineAndPlane(line = [[0,0,0],[1,1,1]], plane = [1, 2, 3, 4]):
    """
    

    Parameters
    ----------
    line : TYPE-> list of 2 sublists
        DESCRIPTION-> The list of 2 sublists where first sublist is a 
        list of coordinates of the point line passing through and second 
        sublist is a list of direction ratios of the line.
        The default is [[0,0,0],[1,1,1]].
    plane : TYPE-> list
        DESCRIPTION -> list of 3 direction ratios of the normal of 
        the plane and the intercept. 
        The default is [1, 2, 3, 4]..

    Returns
    -------
    result : TYPE-> degree
        DESCRIPTION-> Angle between a line and a plane.
        
    Example:
        Find the angle between the planes,
                x + 3 = y - 5 = z + 6
        line: ------  ------  ------ 
                  2       4       2
                  
        plane: x + y + z = 1
                  
        Formula:
           sin θ =  | b . n |
                   ______________
                    | b || n |
                    
	>>from d3g.angle import lineAndPlane
        >>lineAndPlane(line = [[0,0,0],[1,1,1]], plane = [1, 2, 3, 4])
        70.52877936550934

    """
    
    plane=plane[:-1]
    numerator=abs(dotProduct(line[1], plane))
    denominator=magnitude(line[1])*magnitude(plane)
    result=numerator/denominator
    result=180*math.asin(result)/math.pi
    return result
    
