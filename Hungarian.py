import numpy as np
from scipy.optimize import linear_sum_assignment

# Generate a distance matrix for 4 cities
distances = np.array([[0, 2, 9, 10],
                      [1, 0, 6, 4],
                      [15, 7, 0, 8],
                      [6, 3, 12, 0]])

# Set diagonal to infinity to avoid self-loops
np.fill_diagonal(distances, 999)

# Solve the assignment problem
row_ind, col_ind = linear_sum_assignment(distances)

# Construct the optimal tour
tour = []
for i in range(4):
    j = col_ind[i]
    tour.append((i, j))

# Print the tour and its cost
print("Tour:", tour)
print("Cost:", distances[row_ind, col_ind].sum())