value = 20  # per dozen
demand = 34300  # per year
costOrder = 10 # per order
costHold = 0.4 

Q = ((2 * demand * costOrder) / costHold) ** 0.5

print("Economic order Quantity is", round(Q,2), "dozens")

yearlyOrders = demand/Q
tvc = Q * costHold * yearlyOrders * 0.5 #total holding cost
print("Total Inventory Cost: ${:,.2f}". format(tvc))


