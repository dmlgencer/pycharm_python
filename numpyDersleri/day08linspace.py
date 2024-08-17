import numpy as np


# linspace de başlangıç ve bitiş dahildir iki bilgiyi de veririz kaç parçaya böleceğini de veririz
print(np.linspace(1, 20, 10))

bol=np.linspace(5,8,4)
print(bol, "\n")
print(bol[1]- bol[2])