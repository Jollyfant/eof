import numpy as np
import matplotlib.pyplot as plt

from src.loader import loadDataFiles
from src.linalg import detrend, normalize, getFEOF, getEOF, getCovariance
from src.plot import plotEigenvalues, plotDouble

directory = "forward/traces"

if __name__ == "__main__":

  # Load forward modelled data files
  datas = loadDataFiles(directory)
  means = detrend(datas)

  plt.scatter(means[0], means[-1])
  plt.xlabel("Station 1 (g)")
  plt.ylabel("Station 2 (g)")
  plt.show()
  # Fast EOF using covariance matrix instead of SVD
  w, v = getFEOF(means)

  cutoff, importance = normalize(w)

  # Plot the importance of the eigenvectors
  plotEigenvalues(importance)

  # Cutoff some non-important EOFs
  v = v[:,0:cutoff] 

  plotDouble(importance, means, v)
