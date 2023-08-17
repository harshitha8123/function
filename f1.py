import numpy as np
arr=np.array([[2,3,4],[1,6,5]])
print("sum of the array=",arr.sum())
print("maxzimum of array=",arr.max())
print("minimum of array=",arr.min())
print("minimum array in columns=",arr.min(axis=1))
print("maxzimum array in  columns=",arr.max(axis=1))
print("cumelative sum of array=",arr.cumsum(axis=1))
print("Avrage of array=",arr.mean())
