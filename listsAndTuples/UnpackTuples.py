
fruits = ("apple", "banana", "strawberry", "cherry")
(a , b, *c ) = fruits # burada a b c sembollerine sırayla apple banana ve strawberry denk geliyor. 0c ise 0 ve 1. index a be b ye denk geldiği için geriye kalan tüm elemanları temsil ediyor.
print(a)# apple
print(b)# banana
print(c)# ['strawberry', 'cherry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)# apple
print(tropic)# ['mango', 'papaya', 'pineapple']
print(red)# cherry

for i in fruits:
    print(i)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)#('a', 'b', 'c', 1, 2, 3)