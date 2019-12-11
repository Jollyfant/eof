import numpy as np
import matplotlib.pyplot as plt

from src.loader import loadDataFiles
from src.linalg import detrend, normalize, getFEOF, getEOF, getCovariance
from src.plot import plotEigenvalues, plotPCA, plotEOF

directory = "/Users/koymans/Documents/phd/code/forward/traces"

if __name__ == "__main__":

  datas = loadDataFiles(directory)
  means = detrend(datas)

  # Fast EOF using covariance matrix instead of SVD
  w, v = getFEOF(means)

  cutoff, importance = normalize(w)

  # Plot the importance of the eigenvectors
  plotEigenvalues(importance)

  # Cutoff some non-important EOFs
  v = v[:,0:cutoff] 

  plotEOF(v)
  plotPCA(means, v)
