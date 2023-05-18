arrivalRate = 30 #trains per day
serviceTime = 36 #minutes

lam = arrivalRate/(60*24) #convert to per minute
mew = 1/serviceTime #hours per train

roh = lam/mew

lenQ = lam / (mew - lam)

print("Length of queue =", lenQ)
if(lenQ%1 != 0):
    print("Queue is between",int(lenQ),"and",int(lenQ)+1)

prob = roh**10
print("Probability that queue exceedes 10 trains is",round(prob,2))
