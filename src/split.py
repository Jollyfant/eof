def splitTrace(trace, on):

  # Length of the trace in seconds
  length_seconds = len(trace)

  # Calculate the number of equal parts to split the array in
  number_equal_parts = length_seconds / on

  return np.split(trace, number_equal_parts)

def averageTrace(trace):

  traces1 = splitTrace(trace1, 60)
  mean1 = np.std(traces1, axis=1)

  traces2 = splitTrace(trace1, 3600)
  mean2 = np.mean(traces2, axis=1)

  traces3 = splitTrace(trace1, 24 * 3600)
  mean3 = np.mean(traces3, axis=1)

  return mean1, mean2, mean3
