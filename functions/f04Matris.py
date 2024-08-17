'''
- Kullanıcıdan matris bilgilerini aldık ve matris görünümünde bastırdık.
'''


def matris_oluştur(satir, sutun):
    matris = []
    for i in range(satir):
        satir = []
        for j in range(sutun):
            deger = int(input(f"Matrisin {i + 1}. satırın {j + 1}. elemanını girin: "))
            satir.append(deger)
        matris.append(satir)
    return matris


def matrisi_yazdir(matris):
    for satir in matris:
        for eleman in satir:
            print(eleman, end="\t")
        print()


satirSayisi = int(input("Matrisin satir sayisini giriniz: "))
sutunSayisi = int(input("Matrisin sutun sayisini giriniz: "))

matris = (matris_oluştur(satirSayisi, sutunSayisi))
print("Oluşturulan matris: ")
matrisi_yazdir(matris)


# Matristeki elemanların toplamını bulan fonksiyon:
def matris_toplami(matris):
    toplam = 0
    for satir in matris:
        for eleman in satir:
            toplam += eleman
    return toplam


toplam = matris_toplami(matris)
print("Matristeki elemanların toplamı: ", toplam)
