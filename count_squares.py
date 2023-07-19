"""
input: [[1,1], [0,0], [1,0], [0,1], [-4,2], [-2,-1], [-1,4]]
output: 2

trick: is to find the mid point of the square and then find the other two points
"""

# o(n^2) in time | o(n) in space
def countSquares(points):
    pointsSet = set()
    for point in points:
        pointsSet.add(point_to_str(point))

    count = 0
    for point_a in points:
        for point_b in points:
            if point_a == point_b:
                continue

            mid_point = [(point_a[0] + point_b[0]) / 2 , (point_a[1] + point_b[1]) / 2]
            x_dist_mid = point_a[0] - mid_point[0]
            y_dist_mid = point_a[1] - mid_point[1]

            point_c = [mid_point[0] + y_dist_mid, mid_point[1] - x_dist_mid]
            point_d = [mid_point[0] - y_dist_mid, mid_point[1] + x_dist_mid]

            if point_to_str(point_c) in pointsSet and point_to_str(point_d) in pointsSet:
                count += 1
    
    return count / 4

def point_to_str(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point =  [int(cor) for cor in point]
    return ",".join([str(point[0]), str(point[1])])