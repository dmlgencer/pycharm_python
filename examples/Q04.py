
'''

Kullanıcıdan vize ve final bilgilerini al.
vizenin %40 ı finalin %60 ı olsun. 60 ı geçemiyorsa kaldı geçtiyse geçti desin.

'''



def gecmeNotu(v, f):
    gecmeNotu = v * 0.4 + f * 0.6

    if v < 0 or f < 0:
        print("Lütfen geçerli bir not giriniz: ")
    if gecmeNotu>=60:
        print("Geçme Notu: " , (v * 0.4 + f * 0.6))
    else:
        print("Kalma Notu: ", (v * 0.4 + f * 0.6))

    print(type(gecmeNotu))


while True:

    vize = int(input("Vize notunu giriniz: "))
    final = int(input("Final notunu giriniz: "))
    gn = gecmeNotu(vize, final)


