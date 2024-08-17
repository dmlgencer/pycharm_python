'''

5-) Kullanıcının girdiği iki sayı birbirine eşitse bu sayının 4’de göre modunu alıp ekrana yazdıran python kodlarını yazınız?
'''


def equalityControl(x, y):
    if x==y:
        print("The mode of the fist number according to 4 : ", (x%4))
        print("The mode of the second number according to 4 : ", (y%4))



while True:
    s1 = input("Enter the first number: ")
    if not s1.isdigit():
        print("Please enter the just number ")
        break
    s2 = input("Enter the second number: ")
    if not s2.isdigit():
        print("Please enter the just number ")
        break
    s1 = int(s1)
    s2 = int(s2)
    if s1==s2:
        equalityControl(s1, s2)

