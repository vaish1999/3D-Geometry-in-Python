#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 02:08:56 2020

@author: Vaishakh
"""

def magnitude( vector = [1, 2, 3] ):
    """
    

    Parameters
    ----------
    vector : TYPE-> list
        DESCRIPTION-> list of direction ratios of a given vector. 
        The default is [1, 2, 3].

    Returns
    -------
    result : TYPE-> float
        DESCRIPTION-> Magnitude of a given vector.
        
    Example:
        Find the magnitude of the vector v = 5i + 3j - 4k
        
        Formula:
            √ ( A**2 + B**2 + C**2 )
        
        >>from d3g.vector import magnitude
        >>magnitude(vector = [ 5, 3, -4 ])
        7.0710678118654755
        
    """
    
    result=0
    for i in vector:
        result+=i**2
    result=result**0.5
    return result

def dotProduct(vector1 = [1, 2, 3], vector2 = [2, 3, 1]):
    """
    

    Parameters
    ----------
    vector1 : TYPE-> list
        DESCRIPTION-> list of direction ratios of a given vector. 
        The default is [1, 2, 3].
    vector2 : TYPE-> list
        DESCRIPTION-> list of direction ratios of a given vector. 
        The default is [2, 3, 1].

    Returns
    -------
    result : Datatype of the content of the list
        DESCRIPTION-> The dot product of two vectors.
        
    Example:
        Find the dot product of the vectors i + 2j + 3k and 2i + 3j + k
        
        >>from d3g.vector import dotProduct
        >>dotProduct(vector1 = [1, 2, 3], vector2 = [2, 3, 1])
        11

    """
    
    result=0
    for i,j in zip(vector1,vector2):
        result+=i*j
    return result

def crossProduct(vector1 = [1, 2, 3], vector2 = [2, 3, 1]):
    """
    

    Parameters
    ----------
    vector1 : TYPE-> list
        DESCRIPTION-> list of direction ratios of a given vector. 
        The default is [1, 2, 3].
    vector2 : TYPE-> list
        DESCRIPTION-> list of direction ratios of a given vector. 
        The default is [2, 3, 1].

    Returns
    -------
    result : list
        DESCRIPTION-> The list of direction ratios of the 
        cross product of two vectors.
        
    Example:
        Find the cross product of the vectors i + 2j + 3k and 2i + 3j + k
        
        >>from d3g.vector import crossProduct
        >>crossProduct(vector1 = [1, 2, 3], vector2 = [2, 3, 1])
        [-7, 5, -1]

    """
    a=vector1[0]
    b=vector1[1]
    c=vector1[2]
    d=vector2[0]
    e=vector2[1]
    f=vector2[2]
    result=[b*f-c*e,-(a*f-c*d),a*e-b*d]
    return result


    
