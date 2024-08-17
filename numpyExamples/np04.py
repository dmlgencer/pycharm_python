#İki numpy dizisi oluşturun ve bu diziler üzerinde toplama, çıkarma, çarpma ve bölme işlemleri yapın. Sonuçları ekrana yazdırın.

import numpy as np
arr = np.array([1,4,5,6,3])
drr = np.array([9,5,1,8,9])


print(arr[0] + drr[0], "\n")
print(drr[3] - arr[2], "\n")
print(arr[0]*drr[2], "\n")
print(arr[2]/drr[0], "\n")