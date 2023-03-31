
import numpy as np

cost_matrix = np.array([[19,30,50,10],
                        [70,30,40,60],
                        [40,8,70,20]])
supply = np.array([7,9,18])
demand = np.array([5,8,7,14])

allocation_matrix = np.zeros((3, 4))

while np.sum(supply) > 0 and np.sum(demand) > 0:
    min_index = np.unravel_index(np.argmin(cost_matrix), cost_matrix.shape)
    allocation = min(supply[min_index[0]], demand[min_index[1]])
    allocation_matrix[min_index] = allocation
    supply[min_index[0]] -= allocation
    demand[min_index[1]] -= allocation
    cost_matrix[min_index] = 9999

cost_matrix = np.array([[19,30,50,10],
                        [70,30,40,60],
                        [40,8,70,20]])

print(allocation_matrix)
total_cost = np.sum(allocation_matrix * cost_matrix)
print("Total Cost:", total_cost)

