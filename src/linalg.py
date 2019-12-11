import numpy as np

def getFEOF(matrix):

  # Eigenvectors of the covariance matrix
  # Decompose symmetric matrix using eigh
  return np.linalg.eigh(getCovariance(matrix))

def getEOF(matrix):

  return np.linalg.svd(matrix)

def getCovariance(array):

  """
  def getCovariance
  Returns covariance matrix of a matrix
  """

  # Factor
  f = (1. / (1 - len(array[0])))

  # Normalized covariance matrix
  return f * array @ array.T

def reconstructDecomposition(w, v):

  """
  def reconstructDecomposition
  Reconstructs the eigendecomposition
  """

  # ULU'
  return v @ np.diag(w) @ v.T

def detrend(array):

  """
  def removeMeans
  Removes means from timeseries
  """

  # Demean the arrays
  return array - np.mean(array, axis=1, keepdims=True)

def normalize(array):

  CUTOFF = 0.999

  # Normalize
  importance = np.cumsum(array / np.sum(array))
  return np.argmax(importance > CUTOFF), importance
