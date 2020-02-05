import numpy as np
from grid import Grid
import matplotlib.pyplot as plt

if __name__ == "__main__":

  length = 3600
  nx = 5
  ny = 5

  # Create a rectangular grid of 100x100 points with size 10km
  g = Grid(10E3, nx, ny)

  # Solve timesteps with particular solution
  traces = g.solveSteps(length, g.getCheckboardSolution)

  i = 0

  for x, row in zip(g.x, traces):
   for y, column in zip(g.y, row):

     filename = "/Users/koymans/Documents/phd/code/forward/traces/" + "trace-%s" % str(i).zfill(3)
     np.savetxt(filename, column)
     i += 1
