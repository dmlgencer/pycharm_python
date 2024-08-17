import numpy as np

# index ve slice

vector = np.array([0,2,4,5,6,7,8,15])
print(vector[0])
print(vector[3])
print(vector[-1])
print(vector[1:3])# substring gibi 1 dahil 3 dahil değil 1 den 3 e kadar yani 2,4
print(vector[2:6:2]) # 2 den 6 ya kadar 2 dahil 6 dahil değil. 2 şer 2 şer atlayarak gidiyor
print(vector[:5])# en baştan 5 dahil demek 