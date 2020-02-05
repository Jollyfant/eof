import numpy as np
import matplotlib.pyplot as plt
from position import Position
from sources import MogiPointSource

class Grid():

  G = 6.67E-11
  v = 0.25
  rho = 2800
  noise = 10

  """
  class Grid
  Creates a (nx, ny) grid on which gravity from a source
  will be evaluated
  """

  def __init__(self, size, nx, ny):

    # Number of points in grid
    self.nx = nx
    self.ny = ny
    self.size = size

    # Create the grid spacings
    self.x = np.linspace(0, size, nx)
    self.y = np.linspace(0, size, ny)

    # Grid points are on a flat surface
    self.z = 0

  def solveSteps(self, n, function):

    slices = list()

    for t in np.linspace(0, 1, n):
      slices.append(function(t))

    return np.dstack(np.array(slices))

  def getSingleSolution(self, t):

    # Ascending mass based on fraction of t
    #z = (t * 3000) - 4000
    z = -4000
    x = 10000 * t
    y = 10000 * t

    source = MogiPointSource(
      Position(x, y, z),
      1E11,
      0,
    )
  
    return self.gridSolve(source)
  
  def getCheckboardSolution(self, t):
  
    """
    def getCheckboardSolution
    Returns a source checkboard pattern
    """

    nx = 3
    ny = 3

    # Empty container for the summed gravity effects
    solution = np.zeros((self.nx, self.ny))
  
    for x in np.linspace(0, self.size, nx):
      for y in np.linspace(0, self.size, ny):
  
        # Ascending mass based on fraction of t
        z = (t * 3000) - 4000

        source = MogiPointSource(
          Position(x, y, z),
          1E12,
          0 
        )
  
        solution += self.gridSolve(source)
  
    return solution


  def createSeries(self, x, y, sources):

    return values + np.random.normal(0, 1, len(values))

  def gridSolve(self, source):

    """
    def Grid.fsolve
    Fast vectorized solver of gravity grid
    """

    # Mogi point source volume change
    mogi = ((source.dm / self.rho) * (1 - self.v) / np.pi)

    # Subtract the source position from receiver positions
    dx = self.x - source.position.x 
    dy = self.y - source.position.y
    dz = self.z - source.position.z

    # Create a meshgrid
    gx, gy = np.meshgrid(dx, dy)

    # Vectorized solve for distance to source
    r2 = (gx ** 2 + gy ** 2 + dz ** 2) ** (3/2)

    # Vertical displacement because of volume change
    mz = mogi * (dz / r2)

    # Bouguer slab approximation
    bg = 2 * np.pi * 2800 * mz

    # Free air gradient
    fag = 308.6 * mz

    noise = self.noise * np.random.rand(self.nx, self.ny)

    return noise - fag + (1E8 * self.G * (((source.mass + source.dm) * dz / r2) + bg))
