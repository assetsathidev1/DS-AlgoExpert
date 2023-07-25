"""
input: [
  [1, 1],
  [2, 2],
  [3, 3],
  [0, 4],
  [-2, 6],
  [4, 0],
  [2, 1]
]
output: 4
"""

# Incorrect solution - partially correct
import math
def lineThroughPoints(points):
    slopes_dict = {}
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if (points[j][0] - points[i][0]) == 0:
                m = "unf"
                # print("unf:", points[j], points[i])
                c = "unf"
            else:    
                m = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                c = points[i][1] - (m*points[i][0])
            
            mc = (m,c)
            if mc in slopes_dict:
                slopes_dict[mc] += 1
            else:
                slopes_dict[mc] = 1
    print(slopes_dict)
    max_points = 0
    max_slope = None
    for k in slopes_dict:
        if slopes_dict[k] > max_points:
            max_points = slopes_dict[k]
            max_slope = k
    print(max_slope, max_points)
    return math.ceil(max_points/2) + 1
