# liste bu şekilde oluşturuluyor.
courses = ["History", "Math", "Physics", "Computer Science"]
print(courses)

print(courses[0])  # History
print(courses[3])  # Computer Science
print(courses[-1])  # negatif yazarsan da HER ZAMAN sondaki değeri basar.
print(courses[0:2])  # 1. değer dah,l 2. değer dahil değil ==> History, Math
print(courses[:2])  # History, Math
print(courses[2:])  # 2. index ve sonrasını alıyor. ==> Physics, Computer Science

# listeye eleman ekleyelim

# append() metodu listeye eleman eklemek istediğimizde kullanılır. Ama listeye ekleman eklerken bunu HER ZAMAN EN SONA ekler.
courses.append("Art")
print(courses)  # değer en sona eklendi

# eklemek istediğimiz değeri en başa eklemek istersek insert() metodunu kullanıırz.
courses.insert(0, "Graph Theory")  # en başa eklendi
print(courses)

# iki listeyi birleştirmek için extend() metodu kullanılır. Ama her zaman en sona ekleme yapar
courses2 = ["Damla", "Berkay"]
courses.extend(courses2)
print(courses)  # ['Graph Theory', 'History', 'Math', 'Physics', 'Computer Science', 'Art', 'Damla', 'Berkay']

# listeden eleman silmek için remove() kullanılır.
courses.remove("Math")
print(courses)

# listede sondaki elemanı silmek için pop() metodu kullanılır.
popped = courses.pop()
print(popped)
print(courses)  # Berkay listeden silinmiş oldu

# Listedeki elemanları SONDAN BAŞA sıralayalım
courses.reverse()
print(courses)

# listedeki elemanları A-Z şeklinde sırayalım
courses.sort()
print(courses)

# sayısal liste için işlemler
numbers = [3, 7, 1, 9, 8, 0]
numbers.sort()  # küçükten büyüğe sıralar
print(numbers)

numbers.reverse()  # büyükten küçüğe sıralar
print(numbers)

numbers.sort(reverse=True)  # bu kullanım da doğrudur.
print(numbers)

print(min(numbers))  # listedeki en küçük değeri döndürür
print(sum(numbers))  # listedeki değerleri toplar
print(courses.index("History"))  # kaçıncı indexte olduğunu verir.
print("Art" in courses)  # true
print("Math" in courses)  # false


#  courses listesindeki elemanların her birine erişmek için kullanılır.
for w in courses:
    print(w)

# elemanlara indexleri ve yanlarında değerleri ile görmek için
for index, course in enumerate(courses):
    print(index, course)
