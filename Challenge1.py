# def calculatePerimeter(grid, point):
#    """
#    Given an MxN grid of integers and a point in the 0-based grid,
#    calculate the perimeter of the largest island to which that point belongs.
#    An island is a group of horizontally and vertically contiguous cells with the same value.
#    Example:
#    Grid:
#    ---—*****———-----
#    | 0 * 1 * 0 | 0 |
#    —---*—--*———-----
#    | 2 * 1 * 0 | 1 |
#    —---*--—*****—---
#    | 0 * 1 | 1 * 0 |
#    —---*********—---
#    | 1 | 0 | 0 | 3 |
#    ——————-----------
#    Given point: (1, 1)
#    The perimeter here is denot/ed in *'s, and would be 10.
#    @param grid: an MxN array of integers
#    @param point: (x,y) tuple where x is the coordinate which corresponds to the row and y corresponds to the column
#    @return: perimeter
#    """
#    perimeter = None

#    # Your code goes here
#    return perimeter	
  





# Python 3 program to calculate perimeter of the largest 
# island to which the point grid belongs

#An M * N array of intergers
M = 4
N = 4

# Function taking three perimeters to calculate the perimeter
# of the largest island/number
def calculatePerimeter(grid, x, y):

    count = 0

    # x and y-coordinates corresponding to the rows and column
    if (x > 1 and grid[x - 1][y]):
        count += 1

    if (y > 1 and grid[x][y - 1]):
        count += 1

    if (x < M-1 and grid[x + 1][y]):
        count += 1

    if (y < N-1 and grid[x][y + 1]):
        count += 2

    return count

#Function that returns sum of perimeter of the rows and column and
#taking grid(whole array) as a perimeter
def returnPerimter(grid):

    perimeter = 0

    # Traversing the matrix and finding ones to
    # calculate their contribution.
    for x in range(1, M):
        for y in range(1, N):
            if (grid[x][y]):
                perimeter += (3 - calculatePerimeter(grid, x, y))

    return perimeter

# Driver code or declaring a grid for containing our nested arrays
grid = [[0, 1, 0, 0],
        [2, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 0, 3]
        ]

#Printing out our result 
print(returnPerimter(grid))
