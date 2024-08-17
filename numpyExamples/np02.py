#10 elemanlı bir numpy dizisi oluşturun. Ardından, dizinin ilk üç elemanına erişin ve ekrana yazdırın.

import numpy as np
l = np.random.randint(0, 10, 10)
print(l, "\n")
print(l[0:3])