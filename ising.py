import math
import random
import numpy as np
import matplotlib.pyplot as plt


def valid_neighbors(x, y, grid_size):
    x_options = [x - 1, x, x + 1]
    y_options = [y - 1, y, y + 1]
    # options = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    valid_x = []
    valid_y = []
    for i in x_options:
        for k in y_options:
            if 0 <= i < grid_size:
                if 0 <= k < grid_size:
                    if i != x or k != y:
                        valid_x.append(i)
                        valid_y.append(k)
    return valid_x, valid_y


def run_simulation(size, iterations, j, beta):
    grid = np.random.randint(2, size=(size, size))
    grid = grid * 2 - 1
    activity = []
    for iter in range(iterations):
        i_coords = [x for x in range(size)]
        k_coords = [x for x in range(size)]
        random.shuffle(i_coords)
        random.shuffle(k_coords)
        for i in i_coords:
            for k in k_coords:
                node = grid[i, k]
                neighbors_x, neighbors_y = valid_neighbors(i, k, size)
                num_neighbors = len(neighbors_x)
                H_original = 0
                H_alt = 0
                for n in range(num_neighbors):
                    H_original += grid[neighbors_x[n], neighbors_y[n]] * node
                    H_alt += grid[neighbors_x[n], neighbors_y[n]] * node * -1
                H_original *= -j
                H_alt *= -j
                if H_alt < H_original:
                    grid[i, k] = -node
                else:
                    if random.random() < math.e**(-beta*(H_alt - H_original)):
                        grid[i, k] = -node
        active = 0
        for r in grid:
            for x in r:
                if x == 1:
                    active += 1
        activity.append(active)
    return activity
        # if iter % 5 == 0:
        #     plt.matshow(grid)
        #     plt.show()


def main(size, iterations, j, beta):
    for beta in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        activity = run_simulation(size, iterations, j, beta)
        plt.plot(activity)
        plt.title(j)
        plt.show()


if __name__ == '__main__':
    size = 20
    iterations = 200
    j = 0.7
    beta = 0.5
    main(size, iterations, j, beta)
