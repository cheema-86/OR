import numpy as np
from scipy.optimize import linear_sum_assignment

# Generate random distance matrix
n = 5
distances = np.array([[ 1, 10, 20, 30, 40],
                      [10,  1, 15, 25, 35],
                      [20, 15,  1, 14, 24],
                      [30, 25, 14,  1, 18],
                      [40, 35, 24, 18,  1]])
#distances = np.random.rand(n, n)

# Set diagonal to infinity to avoid self-loops
np.fill_diagonal(distances, 999)

# Solve the assignment problem
row_ind, col_ind = linear_sum_assignment(distances)

# Construct the optimal tour
tour = []
i = 0
for count in range (n-1):
    j = col_ind[i]
    if j == 0:
        j = i+1
    tour.append((i,j))
    i = j
tour.append((j,0))

'''
for i in range(0,n-1):
    j = col_ind[i]
    tour.append((i, j))
'''
    
# Print the tour and its cost
print("Tour:", tour)

cost = 0
for x in range (len(tour)):
    cost += distances[tour[x][0],tour[x][1]]

print("Cost:", cost)