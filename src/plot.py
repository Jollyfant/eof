import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from scipy.interpolate import griddata

def plotEigenvalues(eig):

  """
  def plotEigenvalues
  Plots relative importance of eigenvalues
  """

  plt.title("EOF mode weights (eigenvalues)")
  plt.semilogy(eig)
  plt.scatter(np.arange(len(eig)), eig)
  plt.show()

def plotDouble(importance, means, eigenvectors):

  coefficients = means.T @ eigenvectors

  for i, (weight, vector, coefficient) in enumerate(zip(importance, eigenvectors.T, coefficients.T)):

    matrix = np.split(vector, np.sqrt(len(eigenvectors)))

    plt.suptitle("EOF & PCA %i with weight %.5f" % (i, weight))

    plt.subplot(2, 1, 1)
    dx = 2500
    extent = [-dx, 10000 + dx, 10000 + dx, -dx]
    plt.imshow(matrix, interpolation="lanczos", cmap="jet", aspect="auto", extent=extent)
    plt.colorbar(orientation="horizontal")

    plt.subplot(2, 1, 2)
    plt.plot(coefficient)
    
    plt.show()
