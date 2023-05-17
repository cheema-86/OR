year = [1,2,3,4,5]
resaleValue = [42000, 30000, 20400, 14400, 9650]
spareCost = [4000, 4270, 4880, 5700, 6800]
labourCost = [14000, 16000, 18000, 21000, 25000]

cumCost = [spareCost[i]+labourCost[i] for i in range (0,5)]
for i in range (1,5):
    cumCost[i] += cumCost[i-1] 

depCost = [60000-i for i in resaleValue]

totalCost = [cumCost[i]+depCost[i] for i in range (0,5)]

avgCost = [totalCost[i]/year[i] for i in range (0,5)]

minCost = min(avgCost)
repYear = year[avgCost.index(minCost)]

print("Year:",year)
print("Cummulative Cost:",cumCost)
print("Depreciation Cost:",depCost)
print("Total Cost:",totalCost)
print("Average Cost:",avgCost)
print("----------")
print("Min avg cost:", minCost)
print("Machine should be replaced after", repYear,"years")

