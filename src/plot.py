import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from scipy.interpolate import griddata

def plotEigenvalues(eig):

  """
  def plotEigenvalues
  Plots relative importance of eigenvalues
  """

  plt.plot(eig)
  plt.scatter(np.arange(len(eig)), eig)
  plt.show()

def plotEOF(eigenvectors):

  """
  def plotEOF
  Plots the empirical orthonormal functions in space
  """

  for vector in eigenvectors.T:
    matrix = np.split(vector, np.sqrt(len(eigenvectors)))
    plt.imshow(matrix, interpolation="lanczos", cmap="jet")
    plt.colorbar()
    plt.show()

def plotDouble(importance, means, eigenvectors):

  coefficients = means.T @ eigenvectors

  for i, (weight, vector, coefficient) in enumerate(zip(importance, eigenvectors.T, coefficients.T)):

    matrix = np.split(vector, np.sqrt(len(eigenvectors)))

    plt.suptitle("EOF & PCA %i with weight %.5f" % (i, weight))

    plt.subplot(2, 1, 1)
    plt.imshow(matrix, interpolation="lanczos", cmap="jet", aspect="auto")
    plt.colorbar(orientation="horizontal")

    plt.subplot(2, 1, 2)
    plt.plot(coefficient)
    
    plt.show()
  
def plotPCA(means, eigenvectors):

  """
  def plotPCA
  Plots the principal components (expansion coefficients)
  """

  coefficients = means.T @ eigenvectors

  for coefficient in coefficients.T:
    plt.plot(coefficient)
    plt.show()
