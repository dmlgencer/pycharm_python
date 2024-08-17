
'''

kullanıcıdan 4 işlem için 2 adet sayı iste
4 adet fonksiyon olsun
toplama, çıkarma, çarpma, bölme


'''
from numpy._core.defchararray import isdigit

giris="""
1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
"""


def toplama(x, y):
    return print("Sayıların Toplamı: ", x+y)


def cikarma(x, y):
    return print("Sayıların Farkı: ", x-y)


def carpma(x, y):
    return print("Sayıların Çarpımı: " , x*y)


def bolme(x, y):
    if y==0:
        print("Sıfır paydada yer alamaz.")
    return print("Sayıların Bölümü: ", x/y)



while True:
    print("Çıkış için q tuşuna basınız :")
    s1 = (input("1. sayıyı giriniz: "))
    s2 = (input("2. sayıyı giriniz: "))
    if not isdigit(s1) or not isdigit(s2):
        print("Lütfen sayı değeri giriniz. ")
        continue



    if s1.islower()=='q' or s2.islower()=='q':
        break
    s1 = int(s1)
    s2 = int(s2)
    print(giris)
    sorgu = int(input("Yapmak istediğiniz işlem tipini seçiniz: "))

    if sorgu ==1:
        print(toplama(s1, s2))
    if sorgu ==2:
        print(cikarma(s1,s2))
    if sorgu ==3:
        print(carpma(s1,s2))
    if sorgu==4:
        print(bolme(s1,s2))

