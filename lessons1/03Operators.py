
# type() metodu veri tipinin ne olduğunu söyler. Bu kısım  JavaScripte benziyor.
num = 3
print(type(num))  # int

'''
    Java'da kullanılan operatörlerin 4 işlem için olanlar aynı.
    // ==> Bu sembol bölümü bulduruyor.
    % ==> Bu sembol bölümünden kalanı bulduruyor. 
    ** ==> üs alıyor.
'''

print(7 // 2)  # 3
print(7 % 2)  # 1
print(4 ** 3)


# abs() mutlak değer demek.
print(abs(-4))  # 4


# round() metodu soldaki sayıyı en yakın sayıya yuvarlıyor.
print(round(3.75, 1))  # soldaki double olduğu için 3.8 e yuvarlıyor.



# stringler birleşecekse yan yana yazılır. Matematik işlemi gibi ekleme yapılamaz.
num_1 = "100"
num_2 = "200"
print(num_1 + num_2)  # 100200



#typeCasting yaparak string olan ifadeleri int veri tipine çevirdik.
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)#300
