
import numpy as np

print(np.identity(5), "\n") # köeşegen matris yapar köşegeni 1 lerden oluşan kare matris elde ederiz.
print(np.eye(5, k=3)) # köşegeni 3 birim öteledi
print(np.diag([1,4,5,6])) # köşegene istediğim sayı değerleri beririz. Diagonal den alır adını

r = np.random.randint(0,3,(5,5))
print(r)
print(np.diag(r))# köşegenini bastırdık
print(np.diag(np.diag(r))) # tekrar matris haline getridik 