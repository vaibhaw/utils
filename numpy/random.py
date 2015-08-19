import numpy as np

## random sampling(pick m elements out of n)
# In case of 1D array
# source: http://stackoverflow.com/questions/13335407
# In this case original array will change
np.random.shuffle(array)
n = array.shape[0]
if m<=n:
  subset = array[:m]
else:
  print 'number of points to be sampled should be less than length of array'

# In this case original array will not change
# If m > n, elements in array will repeat
# m can be of any size. e.g. size=(2, 4)
np.random.choice(array, m)

# In case of nD array
# source: http://stackoverflow.com/questions/14262654
