
import numpy as np

# yeniden boyutlandırma

# bu matris normalde 4 e 3 lük.  biz onu bu metod ile 3 e 4 lük hale çevirebiliriz.
m1 = np.array([[1,2,3,4], [5,6,7,8], [9, 10, 11, 12]])


print(m1.shape)

print(m1.size)

print(m1.reshape(4,3))

print(m1.reshape(12))

print(np.random.randint(0,2, (8,6)).reshape(6, 8))
