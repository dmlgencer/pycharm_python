import pandas as pd
'''
What is a Series?
A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.

'''
a = [1.3,5.1,8]  #0    1.3
m = pd.Series(a) #1    5.1
print(m)         #2    8.0   şeklinde bir çıktı görünümü var.



'''
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.
'''
print(m[1])#5.1

'''
Create Labels
With the index argument, you can name your own labels.

'''

m1 = pd.Series(a, index=["x", "y", "z"])#x    1.3
print(m1)                               #y    5.1
                                        #z    8.0   şeklinde x, y,z ataması yaptık gibi bi şey oldu