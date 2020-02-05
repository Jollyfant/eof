import numpy as np

class Position():

  def __init__(self, x, y, z):

    self._ = np.array([x, y, z])

  @property
  def length(self):
    return np.sqrt(self._ ** 2)

  @property
  def x(self):
    return self._[0]

  @property
  def y(self):
    return self._[1]

  @property
  def z(self):
    return self._[2]
