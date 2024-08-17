import numpy as np
from numpy.ma.core import shape

# zeros: sıfırlardan oluşan yapılar getirir.
# ones: birlerden oluşan yapılar getirir.

print(np.zeros(5), "\n")

print(np.zeros((4,4)), "\n")

print(np.ones((3,3)),"\n")

print(np.ones(shape=(3,4)))# istediğim zayılarden ve istediğim şekilde bir matris eldde ettik

print(np.full((4,4), 19))# 4 e 4 lük ve 19 lardan oluşan bir matris elde ettik sabit sayı elde etmek için kullanırız. 0 ve 1 dışında

