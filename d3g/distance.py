#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 01:08:48 2020

@author: Vaishakh
"""

from d3g.vector import magnitude,crossProduct,dotProduct

def _determinant(matrix = [ [1, 0, 0], [0, 1, 0], [0, 0, 1] ]):
    a=matrix[0][0]
    b=matrix[0][1]
    c=matrix[0][2]
    d=matrix[1][0]
    e=matrix[1][1]
    f=matrix[1][2]
    g=matrix[2][0]
    h=matrix[2][1]
    i=matrix[2][2]
    
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))
    

def p2p(p1=(1,1,1),p2=(0,0,0)):
    """
    

    Parameters
    ----------
    p1 :TYPE->tuple
        DESCRIPTION->tuple of coordinates of first point(x1,y1,z1) 
        The default is [1,1,1].
    p2 :TYPE->tuple
        DESCRIPTION->tuple of coordinates of second point(x2,y2,z2) 
        The default is [0,0,0].

    Returns
    -------
    result :TYPE->float
              DESCRIPTION->euclidean distance between the two given points p1 and p2
              
              
    Example: Find the distance between the points (2,1,0) and (5,1,4)
        
	>>from d3g.distance import p2p
        >>p2p(p1=(2,1,0),p2=(5,1,4))
        25.0
        

    """
    
    difference=[i-j for i,j in zip(p1,p2)]
    result=magnitude(difference)
    return result

def pointToPlane(p1=(0,0,0),plane=[1,1,1,1]):
    """
    

    Parameters
    ----------
    p1 : TYPE-> tuple
        DESCRIPTION-> tuple of coordinates of point (x1,y1,z1) 
                      from the respective given plane. 
        The default is (0,0,0).
    plane : TYPE-> list
        DESCRIPTION -> list of 3 direction ratios of the normal of 
        the plane and the intercept. 
        The default is [1,1,1,1].

    Returns
    -------
    result : TYPE-> float
        DESCRIPTION-> distance of the point p1 from the given plane.
        
    Example: Find the distance between the point (1,2,3) and the plane
             2x + 3y + 4z = 1
             
             Formula:
                 distance = | Ax1 + By1 + Cz1 - D |
                            _______________________
                            
                            √ ( A**2 + B**2 + C**2 )
                            
                    where, point->(x1,y1,z1) and plane equation is
                    Ax1 + By1 + Cz1 - D = 0
        
        >>from d3g.distance import pointToPlane
        >> pointToPlane(p1 = (5,2,3), plane = [2,3,4,1])
        0.9310344827586207

    """
    
    numerator,denominator=-plane[-1],0
    for i,j in zip(p1,plane):
        numerator+=i*j
    denominator=magnitude(plane[:-1])
    result=abs(numerator)/denominator
    return result

def pointToLine(p1=(0,0,0),line=[[0,0,0],[1,1,1]]):
    """
    

    Parameters
    ----------
    p1 : TYPE-> tuple
        DESCRIPTION-> tuple of coordinates of point (x1,y1,z1) 
                      from the respective given plane. 
        The default is (0,0,0).
    line : TYPE-> list of 2 sublists
        DESCRIPTION-> The list of 2 sublists where first sublist is a 
        list of coordinates of the point line passing through and second 
        sublist is a list of direction ratios of the line.
        The default is [[0,0,0],[1,1,1]].

    Returns
    -------
    result : TYPE-> float
        DESCRIPTION-> distance of the point p1 from the given line.
        
    Example: Find the distance between the point (1,2,3) and the line
             x + 3 = y - 5 = z + 6
            ------  ------  ------
              2       4       2
            
            Formula:
                
                k = | A(x1 - x2) + B(y1 - y2) + C(z1 - z2) |
                    ________________________________________
                            
                     √ ( A**2 + B**2 + C**2 )
                
                distance = p2p(p1,(A*k + x2, B*k + y2, C*k + z2))
                
        >>from d3g.distance import pointToLine
        >>pointToLine(p1 = (1, 2, 3), line = [ [-3, 5, -6], [2, 4, 2] ])
        14.899105176791087        

    """
    
    numerator,denominator=0,0
    for i,j,k in zip(line[1],p1,line[0]):
        numerator+=i*(j-k)
    denominator=magnitude(line[1])
    k=abs(numerator)/denominator
    pointOnPlane=[]
    for i,j in zip(line[1],line[0]):
        pointOnPlane.append((i*k)+j)
    pointOnPlane=tuple(pointOnPlane)
    result=p2p(p1,pointOnPlane)
    return result
    
def lineToLine(line1=[[0,0,0],[1,1,1]],line2=[[0,0,0],[2,2,2]]):
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
    result : TYPE-> float
        DESCRIPTION-> distance between two lines.
        
    Example:
        Find the distance between the lines:
                x + 3 = y - 5 = z + 6
        line1: ------  ------  ------ 
                  2       4       2
        
                x - 5 = y + 4 = z + 7
        line2: ------  ------  ------ 
                  3       5       1
        
        Formula:
            parallel lines:
                d = | b x (a2 - a1) |
                     ______________
                         | b |
            skew lines:
                d = | (b1 x b2) . (a2 - a1) |
                     ______________________
                         | (b1 x b2) | 
        >>from d3g.distance import lineToLine
        >>lineToLine(line1 = [ [-3, 5, -6], [2, 4, 2] ], line2 = [ [5, -4, -7], [3, 5, 1] ])
        10.9577109184094

    """
    
    difference=[i-j for i,j in zip(line1[0],line2[0])]
    if line1[1]==line2[1]:                          #if lines are parallel
        numerator=crossProduct(difference, line1[1])
        numerator=magnitude(numerator)
        denominator=magnitude(line1[1])
        result=numerator/denominator
        return result
    directionRatioCrossProduct=crossProduct(line1[1], line2[1])
    numerator=abs(dotProduct(directionRatioCrossProduct, difference))             #if lines are skew
    denominator=magnitude(directionRatioCrossProduct)
    result=numerator/denominator
    return result
    
    
