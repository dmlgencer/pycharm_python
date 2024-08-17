# if else kullanarak kişinin reşit olup olmadığını bildiren kod


yas = int(input("Yaşınızı Giriniz: "))

if yas >= 18:
    print("Kişi reşittir.")
elif 18 > yas > 10:
    print("Kişi ergendir.")
else:
    print("Kişi bebektir.")

# Bu kodu for döngüsü ile daha dinamik yaz.

for i in range(1, 6):
    age = int(input("Enter your age: "))
    if age>=18:
        print("Adult")
    elif 18 > age > 10:
        print("Child")
    else:
        print("Baby")



