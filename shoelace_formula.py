# Create a function named getpoints that takes in as an argument a string and returns a list of points of arbitrary
# length.
def getpoints(points):
    points = points.split(" ")
    pointlist = []
    for x in points:
        x = x.split(",")
        for i in range(len(x)):
            x[i] = int(x[i])
        pointlist.append(x)
    return pointlist


# Create a function named cross that takes in two arguments, both of which are a list of one point, and returns the
# cross-product.
def cross(list1, list2):
    return (list1[0] * list2[1]) - (list2[0] * list1[1])


# Create a function named shoelace that takes in as an argument a list of points and returns the area of the polygon
# calculated via the shoelace formula.
def shoelace(points):
    solution = 0
    xy = 0
    yx = 0
    for x in range(len(points)):
        index = (x + 1) % len(points)
        xy += points[x][0] * points[index][1]
        yx += points[x][1] * points[index][0]
    solution += abs(xy - yx)
    solution = solution / 2
    return solution


# Create a function named main that does not take in any arguments nor return any values. This function should take
# an input from the user a string of pairs of numbers separated by commas and spaces, as shown in the format below,
# and print the area of the polygon.
def main():
    vertices = input('Please enter the vertices: ')
    vertices = getpoints(vertices)
    print(f'The area of the polygon is {shoelace(vertices)}')


if __name__ == '__main__':
    main()
