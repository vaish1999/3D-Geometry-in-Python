# 3D-Geometry-in-Python
Explore 3D geometry in python!

This project repo will help you find out the  i. Distances between the two points,two lines and a point and a plane.  ii. Magnitude of a vector, dot product and cross product of two vectors.  iii. Angle between two lines, two planes and a line and a plane.  

Example 1: Find the distance between the points (2,1,0) and (5,1,4)

```python
from 3dg.distance import p2p

p2p(p1=(2,1,0),p2=(5,1,4))

```

Output-

```python
25.0
```

Example 2: Find the distance between the point (1,2,3) and the plane 2x + 3y + 4z = 1

```python
from 3dg.distance import pointToPlane

pointToPlane(p1 = (1,2,3), plane = [2,3,4,1])

```

Output-

```python
3.5282114253639856
```

Example 3: Find the distance between the point (1,2,3) and the line  x + 3 = y - 5 = z + 6
								    ------- ------- -------
								       2       4       2


```python
from 3dg.distance import pointToLine

pointToLine(p1 = (1, 2, 3), line = [ [-3, 5, -6], [2, 4, 2] ])

```

Output-

```python
14.899105176791087
```

Example 4: Find the distance between the lines:         x + 3 = y - 5 = z + 6          x - 5 = y + 4 = z + 7
						 line1:------- ------- -------  line2:------- ------- -------
							  2       4       2		 3       5       1


```python
from 3dg.distance import lineToLine

lineToLine(line1 = [ [-3, 5, -6], [2, 4, 2] ], line2 = [ [5, -4, -7], [3, 5, 1] ])

```

Output-

```python
10.9577109184094
```

Example 5: Find the magnitude of the vector v = 5i + 3j - 4k

```python
from 3dg.vector import magnitude

magnitude(vector = [ 5, 3, -4 ])
```

Output-

```python
7.0710678118654755
```

Example 6: Find the dot product of the vectors i + 2j + 3k and 2i + 3j + k

```python
from 3dg.vector import dotProduct

dotProduct(vector1 = [1, 2, 3], vector2 = [2, 3, 1])
```

Output-

```python
11
```

Example 7: Find the cross product of the vectors i + 2j + 3k and 2i + 3j + k

```python
from 3dg.vector import crossProduct

crossProduct(vector1 = [1, 2, 3], vector2 = [2, 3, 1])
```

Output-

```python
[-7, 5, -1]
```

Example 8: Find the angle between the lines:            x + 3 = y - 5 = z + 6          x - 5 = y + 4 = z + 7
						 line1:------- ------- -------  line2:------- ------- -------
							  2       4       2		 3       5       1

```python
from 3dg.angle import lines

lines(line1 = [ [-3, 5, -6], [2, 4, 2] ], line2 = [ [5, -4, -7], [3, 5, 1] ])
```

Output-

```python
14.963217433307127
```

Example 9: Find the angle between the planes, plane1: x + y + z = 1 plane2: x + 2y + 3z = 4

```python
from 3dg.angle import planes

planes(plane1 = [1, 1, 1, 1], plane2 = [1, 2, 3, 4])
```

Output-

```python
22.207654298596495
```

Example 10: Find the angle between the line and a plane:            x + 3 = y - 5 = z + 6    plane: x + y + z = 1
							     line :------- ------- -------
								      2       4       2

```python
from 3dg.angle import lineAndPlane

lineAndPlane(line = [[0,0,0],[1,1,1]], plane = [1, 2, 3, 4])
```

Output-

```python
70.52877936550934
```



        
        
