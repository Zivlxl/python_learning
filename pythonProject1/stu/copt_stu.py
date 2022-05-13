import sys
import math

from coptpy import *

env = Envr()
model = env.createModel('sudoku')

x = model.addVars(9, 9, 9, vtype=COPT.BINARY)

model.addConstrs((x.sum(i, j, '*') == 1 for i in range(9) for j in range(9)))

model.addConstrs((x.sum(i, '*', v) == 1 for i in range(9) for v in range(9)))

model.addConstrs((x.sum('*', j, v) == 1 for j in range(9) for v in range(9)))

model.addConstrs((quicksum(
    x[i, j, v] for i in range(3 * s, 3 * (s + 1)) for j in range(3 * t, 3 * (t + 1))) == 1 for s in range(3) for t in
                  range(3)
                  for v in range(9)))

f = open(sys.argv[1])

grid = f.read().split()

for i in range(9):
    for j in range(9):
        if grid[i][j] != '.':
            v = int(grid[i][j]) - 1
            x[i, j, v].LB = 1

model.solve()

print("")
print("Solution:")
print("")

solution = model.getInfo(COPT.Info.Value, x)

for i in range(9):
    sol = ''
    for j in range(9):
        for v in range(9):
            if solution[i, j, v] == 1:
                sol += str(v + 1)

    print(sol)
