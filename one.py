# An important part of Statistical Process Control is the Gage RnR
# This library, provided by Alexander Poole, allows the calculation
# of any given dataset with it.

from GaugeRnR import GaugeRnR
import numpy as np

# The input should be structeted in a 3d
# numpy array n[i,j,k] where
# i = operator, j = part, k = measurement
# Example:
#       m1    m2    m3
data = np.array(            #
    [[[3.29, 3.41, 3.64],   # p1 | o1
      [2.44, 2.32, 2.42],   # p2
      [4.34, 4.17, 4.27],   # p3
      [3.47, 3.5, 3.64],    # p4
      [2.2, 2.08, 2.16]],   # p5
     [[3.08, 3.25, 3.07],   # p1 | o2
      [2.53, 1.78, 2.32],   # p2
      [4.19, 3.94, 4.34],   # p3
      [3.01, 4.03, 3.2],    # p4
      [2.44, 1.8, 1.72]],   # p5
     [[3.04, 2.89, 2.85],   # p1 | o3
      [1.62, 1.87, 2.04],   # p2
      [3.88, 4.09, 3.67],   # p3
      [3.14, 3.2, 3.11],    # p4
      [1.54, 1.93, 1.55]]]) # p5

g = GaugeRnR(data)
g.calculate()
print(g.summary())
