

import random

anahtar =1
x = random.randint(0, 10000)
def exit():
    print("İyi Günler Dileriz...")
    quit()

def sifre_kontrol(id):
    if len(id) != 4:
        return False
    if not id[:2].isdigit():  # İlk iki karakterin rakam olup olmadığını kontrol eder
        return False
    if not id[-2:].isalpha():  # Son iki karakterin harf olup olmadığını kontrol eder
        return False
    return True





def mevcutBakiye():

    print("Mevcut Bakiyeniz: ", x)
    sorgu = input("Başka Bir İşlem Yapmak İstiyor Musunuz ?")
    if sorgu == "e" or sorgu == "E":
        print(giris)
    else:
        print("Çıkış Yapılıyor...")
        exit()


def paraCekme():
    global x
    print("Mevcut Bakiyeniz: ", x)
    paraCekmeMiktari = int(input("Çekmek İstediğiniz Miktarı Giriniz: "))
    if (paraCekmeMiktari <= x):
        print("İstediğiniz Miktarı Alabilirsiniz: ")
        a = x-paraCekmeMiktari
        print("Kalan Bakiyeniz: ", a)
        sorgu = input("Başka Bir İşlem Yapmak İstiyor Musunuz ?")
        if sorgu == "e" or sorgu == "E":
            print(giris)
        else:
            print("Çıkış Yapılıyor...")
            exit()

    else:
        print("Çekmek İstediğiniz Miktar Bakiyenizden Fazla. Lütfen Geçerli Miktar Giriniz: ")
        paraCekme()




def paraYatirma():
    global x
    print("Mevcut Bakiyeniz: ", x)
    paraYatirmaMiktari = int(input("Yatırmak İstediğiniz Miktarı Giriniz: "))
    a = paraYatirmaMiktari + x
    print("Yeni Bakiyeniz: ", a)
    sorgu = input("Başka Bir İşlem Yapmak İstiyor Musunuz ?")
    if sorgu =="e" or sorgu =="E":
        print(giris)
    else:
        print("Çıkış Yapılıyor...")
        exit()


def havale():
    global x
    print("Mevcut Bakiyeniz: ", x)

    id = input("Havale Yapmak İstediğiniz Kişinin ID Bilgisini Giriniz: ")
    if len(id) != 4:
        print("ID 4 Basamaklı Olmalıdır. Lütfen Tekrar Deneyiniz: ")
        havale()
    if not id[:2].isdigit():  # İlk iki karakterin rakam olup olmadığını kontrol eder
        print("ID İlk 2 Karakteri Rakam Olmalıdır. Lütfen Tekrar Deneyiniz: ")
        havale()
    if not id[-2:].isalpha():  # Son iki karakterin harf olup olmadığını kontrol eder
        print("ID Son 2 Karakteri Harf Olmalıdır. Lütfen Tekrar Deneyiniz: ")
        havale()
    else:
        print("ID Bilgisi Geçerlidir")

    miktar = int(input("Havale Yapmak İstediğiniz Miktarı Giriniz: "))
    if miktar > x:
        print("Havale Yapmak İstediğiniz Miktar Bakiyenizden Fazla. Lütfen Tekrar Deneyiniz: ")
        havale()

    else:
        print("Havale İşleminiz Başarılı Bir Şekilde Gerçekleşti. ")
        kalanBakiye = x-miktar
        print("Kalan Bakiyeniz: ", kalanBakiye)
        sorgu = input("Başka Bir İşlem Yapmak İstiyor Musunuz ?")
        if sorgu == "e" or sorgu == "E":
            print(giris)
        else:
            print("Çıkış Yapılıyor...")
            exit()


giris = """
(1) Para Çekme  
(2) Para Yatırma
(3) Bakiye Sorgulama
(4) Başka Bir Hesaba Para Yatırma
"""
print(giris)
while True:
    print("WELCOME TO DNG BANK...")

    cevap = (input("Lütfen Yapmak İstediğiniz İşlem İçin Geçerli Numarayı Tuşlayınız (Çıkmak İçin q): "))

    if cevap =="q":
        print("Çıkıyor....")
        break



    if cevap=="1":
        if paraCekme():
            continue



    if cevap=="2":
        if paraYatirma():
            continue

    if cevap=="3":
        if mevcutBakiye():
            continue

    if cevap =="4":
        if havale():
            continue



















