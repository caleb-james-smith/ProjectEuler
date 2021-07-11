# prob_015.py

# Problem 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?
#

from Solver import Solver

def findPaths(width, height):
    n_moves = width + height
    paths = []
    paths.append("")
    for i in range(n_moves):
        new_paths = []
        for p in paths:
            x = p.count('x')
            y = p.count('y')
            if x < width:
                new_paths.append(p + 'x')
            if y < height:
                new_paths.append(p + 'y')
        paths = new_paths
    return paths

def findHalfPaths(width, height):
    n_moves = width + height
    paths = []
    paths.append("")
    for i in range(n_moves):
        new_paths = []
        for p in paths:
            x = p.count('x')
            if x < width:
                new_paths.append(p + 'x')
            # skip y on first iteration
            if i > 0:
                y = p.count('y')
                if y < height:
                    new_paths.append(p + 'y')
        paths = new_paths
    return paths

def solve(dimensions):
    width  = dimensions[0]
    height = dimensions[1]
    if width == height:
        # only find half of paths, then double to get result
        # use symmetry (n x n grid)
        paths = findHalfPaths(width, height)
        n_paths = 2 * len(paths)
    
    else:
        paths = findPaths(width, height)
        n_paths = len(paths)
    
    #print(paths)
    return n_paths

def main():
    solver = Solver(solve, [12, 12])
    solver.solve()

main()

