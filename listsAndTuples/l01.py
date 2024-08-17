

l = ["damla", "dilara", "güzin","gökçe", "hazal", "damla"]
l2 = [3, 4,1 ,2]
l3 = ["damla", 35, True]
print(l) #['damla', 'dilara', 'güzin', 'gökçe', 'hazal', 'damla']
print(len(l))#6
print(type(l))#<class 'list'>
print(type(l2))#<class 'list'>
print(type(l3))#<class 'list'>
l[3] = "berkay"
l.append("emir")# en sona emir i ekler
l.insert(2, "d")# 2. indeksi d yaptı
l.remove("damla")
l.pop(4)
print(l)

# her bir elemana erişmek için
for i in l:
    print(i)

# yeni liste oluşturalım l dekiler oraya geçsin
a = [x for x in l if "a" in x] # tek satırlık bir kullanım
print(a)
b = [x for x in l if x!="damla"]# içinde damla olmayanlar b listesine geçti
print(b)
b.sort()# alfabetik sıraladık
print(b)


