from scipy.optimize import linprog
c = [-3, -2]
A = [[-1, 2],
     [3, 2],
     [1, -1]]
b = [4, 14, 3]

x1_bounds = (0,None)
x2_bounds = (0,None)

res = linprog(c,A_ub=A, b_ub=b, bounds=[x1_bounds,x2_bounds], method='highs')
print(res)