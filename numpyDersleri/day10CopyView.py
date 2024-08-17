

import numpy as np
matris = np.random.randint(0,5, (4,4))
print(matris, "\n")

matris2 = matris.view()

print(matris2, "\n")

matris2[0] = [9,9,9,9]

print(matris2,"\n")
print(matris)

matris3 = np.random.randint(0,5,(4,4))
matris4 = matris3.copy()

matris4[0] =  [7,7,7,7]
print(matris3,"\n")
print(matris4, "\n")