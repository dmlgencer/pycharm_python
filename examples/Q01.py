# kısa ve uzun kenar bilgilerini kullanıcıdan al ve dikdörtgenin alanını ve çevresini hesaplat

a = int(input("Kısa kenar uzunluğunu giriniz: "))
b = int(input("Uzun kenar uzunluğunu giriniz: "))
alan = a*b
cevre = 2*a+2*b
print("Dikdörtgenin alanı: " , alan)
print("Dikdörtgenin çevresi: " ,cevre)