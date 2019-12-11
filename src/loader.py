import os
import json
import numpy as np

def loadDataFiles(directory):

  """
  def loadDataFiles
  Loads forward data files from disk
  """

  # Read the files
  files = os.listdir(directory)
  files = [os.path.join(directory, f) for f in files]

  datas = list()

  # Load the files from disk
  for file in sorted(files):
 
    with open(file, "r") as infile:
      data = json.load(infile)
 
    datas.append(data["trace"])

  return np.array(datas)
