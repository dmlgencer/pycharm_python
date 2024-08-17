
#kullanıcıdan kısa ve uzun kenar bilgilerini aldık fonksiyon yardımıyla da bastırdık
def areaRectangle(x, y):
    return x*y




string = "100"
print("Please enter the information: ")

for i in string:
    k = int(input("Enter the short side information about rectangle: "))
    u = int(input("Enter the long side information about rectangle: "))
    if(k<0):
        print("Please enter the positive number")
    if(u<0):
        print("Please enter the positive number")

    a = areaRectangle(k,u)
    print(a)
