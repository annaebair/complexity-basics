import numpy as np
import random
import matplotlib.pyplot as plt

size = 100
grid = np.zeros((size, size))
p = 0.62
iterations = 400


def valid_neighbors(x, y):
    options = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    neighbors = []
    for opt in options:
        i, j = opt
        if 0 <= i < size:
            if 0 <= j < size:
                neighbors.append(opt)
    return neighbors


# 0: no tree
# 1: tree
# -1: burned tree

# set up grid
for i in range(size):
    for j in range(size):
        if random.random() < p:
            grid[i][j] = 1

# burn bottom layer
for elt in range(size):
    if grid[size-1][elt] == 1:
        grid[size-1][elt] = -1

# burning process
for _ in range(iterations):
    for i in range(size):
        for j in range(size):
            neighbors = valid_neighbors(i, j)
            if grid[i][j] == 1:
                burned_neighbor = False
                for n in neighbors:
                    if grid[n] == -1:
                        grid[i][j] = -1
plt.matshow(grid)
plt.show()
