
list1 = ["History", "Math", "Physics", "Computer Science"]
list2 = list1
print(list1)
print(list2)

# iki liste birbirine bağlı olduğu için list1 deki değişiklik list2 de de değişti.
list1[0] = "Art"
print(list1)
print(list2)

# Tuple olan listelerde değişiklik yapılmaz.
tuple1 = ("History", "Math", "Physics", "Computer Science")
tuple2 = tuple1

print(tuple1)
print(tuple2)

# tuple1[0] = "Damla"  ==> değişikliğe izin vermiyor

