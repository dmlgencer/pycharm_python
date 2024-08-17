#Oluşturduğunuz bir numpy dizisini yeniden şekillendirin.
# Örneğin, 1 boyutlu bir diziyi 2x5 boyutunda bir matrise dönüştürün ve sonucu ekrana yazdırın.
import random
from random import randint

import numpy as np
arr = np.random.randint(0,15, 10)
print(arr, "\n")

# reshape şekil dönüştürmek için kullanılır.
print(arr.reshape(2,5))