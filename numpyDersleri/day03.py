import numpy as np

'''
size: boyut veriyor
shape: şeklini söylüyor kaça kaçlık olduğunu gibi
ndim : uzayda kapladığı boyutu söylüyor. vektör 1 matris 2 boyut mesela 


'''

vector=np.array([1,2,3,4,5,6])
matrix=np.array([[1,2,3],[4,5,6], [7,8,9]])
print(vector)
print(matrix)
print(vector.size)# eleman sayısını söyler
print(matrix.size)
print(vector.shape)
print(matrix.shape)# kaça kaçlık olduğunu gösteriyor
print(vector.ndim) # uzayda kapladığı boyut
print(matrix.ndim)

