# süslü parantezle kullanılıyor.
# 1 elemanı 1 kere yazar.
# her yenilediğinde sırası değişir.
courses = {"History", "Math", "Fizik", "Computer", "Math"}
courses2 = {"History", "Damla", "Fizik", "Education", "Math"}
print(courses)
print(courses.intersection(courses2))  # iki sette ortak olanları döndürür.
print(courses.difference(courses2))  # 1. de olan 2. de olmayanı döndürür.
print(courses.union(courses2))  # ikisini birleştirir.
