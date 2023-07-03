def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]

    for i in range(1, len(coordinates)):
        x2, y2 = coordinates[i]
        slope_x = x2 - x1
        slope_y = y2 - y1

        if slope_x == 0:
            if slope_y != 0:
                return False
        else:
            current_slope = slope_y / slope_x
            if previous_slope is not None and current_slope != previous_slope:
                return False

            previous_slope = current_slope

    return True
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))
