# Python 3 program to calculate perimeter of the largest 
# island to which the point grid belongs

#An MXN array of intergers
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
