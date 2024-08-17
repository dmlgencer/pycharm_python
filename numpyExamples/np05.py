#Bir numpy dizisi oluşturun ve dizideki elemanlardan 5'ten büyük olanları bulun. Bu elemanları ekrana yazdırın.
import numpy as np
matrix = np.array([[5,7,3], [9,2,1], [0, 5,1]])
print(matrix)

for r in matrix:
    for eleman in r:
        if eleman>5:
            print("Eleman: ", eleman)
            print("\n")