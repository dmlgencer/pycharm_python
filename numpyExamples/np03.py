#Oluşturduğunuz bir numpy dizisinin belirli elemanlarını değiştirin. Örneğin, 5. elemanı 100 yapın ve diziyi ekrana yazdırın.
import numpy as np

l = np.random.randint(0, 10, 15)
print(l, "\n")
print(l[4], "\n")
l[4] = 99
print(l[4], "\n")
print(l)
