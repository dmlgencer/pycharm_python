"""
password şartları
1- en az 1 büyük karakter
2- en az 1 küçük karakter
3- şifre en az 8 karakter olmak zorunda
4- 1 adet sayı ve haf dışında bir sembol
"""
import string


def gecerliSifre(cevap):


    rakam = any(char.isdigit() for char in cevap)
    harf = any(char.isalpha() for char in cevap)
    uzunluk = len(cevap)>=8
    sembol = any(char in string.punctuation for char in cevap)


    return rakam, harf, uzunluk, sembol








while True:
    print("Geçerli Şifre Örneği: damlaGencer19*")
    cevap = input("Lütfen Şifrenizi Giriniz: (Çıkış İçin q)")
    rakam, harf, uzunluk, sembol = gecerliSifre(cevap)
    if cevap=='q':
        print("Çıkış Yapılıyor Lütfen Bekleyin....")
        print("Çıkış Yapıldı")
        break
    if rakam and harf and uzunluk and sembol:
        print("Geçerli Şifre!")
        break
    else:
        if not rakam:
            print("Şifrenizde en az 1 adet rakam olmalıdır. ")
        if not uzunluk:
            print("Şifrenizin uzunluğu en az 8 karakter olmalıdır. ")
        if not sembol:
            print("Şifrenizde en az 1 sembol olmalıdır")
        if not harf:
            print("Şifrenizde en az 1 harf olmalıdır. ")
    print("Lütfen tekrar deneyin")




