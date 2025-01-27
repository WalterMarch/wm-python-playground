NUMBER = 100
factorSet = {1, NUMBER}

for i in range(2, NUMBER):
    if NUMBER % i == 0:
        factorSet.add(i)
        factorSet.add(NUMBER // i)

factorList = sorted(factorSet)
print(factorList)
