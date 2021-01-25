import numpy as np
from gekko import GEKKO

m = GEKKO()

m.options.SOLVER = 1

cdc =  # Edit here. Exemple: [[30, 50], [23, 66], [35, 14], [70, 12], [65, 70]]  # Transportation Cost to Intermediate
tcdc =  # Edit here. Exemple: [[12, 25, 22, 40, 41], [65, 22, 23, 12, 15]]  # Transportation Cost form Intermediate to destination
supply =  # Edit here. Exemple: [200, 300, 100, 150, 220]
demand =  # Edit here. Exemple: [150, 100, 110, 200, 180]

v = len(cdc)
w = len(tcdc)

q1 = m.Array(m.Var, (v, w), lb=0, integer=True)
q2 = m.Array(m.Var, (w, v), lb=0, integer=True)


for i in range(len(demand)):
	m.Equation(np.sum(q2, axis=0)[i] >= demand[i])

for i in range(w):
	m.Equation(np.sum(q2[i]) == np.sum(q1, axis=0)[i])

for i in range(len(supply)):
	m.Equation(np.sum(q1[i]) <= supply[i])


def cost(q1, q2, cdc, tcdc, cost=0):
	for i in range(v):
		for k in range(w):
			cost += q1[i][k] * cdc[i][k] + q2[k][i] * tcdc[k][i]
	return cost


m.Minimize(cost(q1, q2, cdc, tcdc))

m.solve()
