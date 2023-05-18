import numpy as np

def northwest_corner_method(supply, demand, costs):
    num_suppliers = len(supply)
    num_customers = len(demand)

    allocation = np.zeros((num_suppliers, num_customers))
    i, j = 0, 0

    while i < num_suppliers and j < num_customers:
        if supply[i] < demand[j]:
            allocation[i][j] = supply[i]
            demand[j] -= supply[i]
            supply[i] = 0
            i += 1
        elif supply[i] > demand[j]:
            allocation[i][j] = demand[j]
            supply[i] -= demand[j]
            demand[j] = 0
            j += 1
        else:
            allocation[i][j] = supply[i]
            supply[i] = 0
            demand[j] = 0
            i += 1
            j += 1

    return allocation

# Example usage
supply = [10, 20, 30]
demand = [20, 10, 20]
costs = np.array([[2, 3, 1],
                  [5, 4, 8],
                  [5, 6, 8]])

allocation = northwest_corner_method(supply, demand, costs)
print("Allocation:")
print(allocation)
