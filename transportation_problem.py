import numpy as np
from gekko import GEKKO

m = GEKKO()
m.options.SOLVER = 1

costs =  # Edit here. Exemple: [[65, 83, 86, 74], [89, 90, 46, 90], [43, 51, 71, 76], [95, 43, 73, 69]]
supply =  # Edit here. Exemple: [243, 379, 490, 122]
demand =  # Edit here. Exemple: [239, 416, 112, 248]
n = len(supply)
p = len(demand)

q = m.Array(m.Var, (n, p), lb=0, integer=True)

for i in range(n):
	m.Equation(np.sum(q[i]) <= supply[i])

for j in range(p):
	m.Equation((np.sum(q, axis=0)[j]) >= demand[j])


def cost(q, costs, cost=0):
	for k in range(n):
		for l in range(p):
			cost += q[k][l] * costs[k][l]
	return cost


m.Minimize(cost(q, costs))

m.solve()
print(q)
