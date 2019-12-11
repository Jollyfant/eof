import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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
    plt.imshow(matrix)
    plt.colorbar()
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
