import numpy as np

'''
dtype : bu kavram verinin tipini söylüyor. int64, float64 gibi 
<U32: içinde 1 tane bile string varsa bunu söndürür. 


'''
sayilar=np.array([1,2,3.0,4,5,"Damla"])
print(sayilar.dtype)# <U32

