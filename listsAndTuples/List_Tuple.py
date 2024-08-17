
#TUPLE DA ELEMAN DEĞİŞTİRMEK İÇİN LİST KULLANDIK

tuple5 = ("damla", "dilara", "güzin","hazal", "ogün")
l = list(tuple5)
l[0] = "ahmet"
tuple5 = tuple(l)
print(l)
print(tuple5)