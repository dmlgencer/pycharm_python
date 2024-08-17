import pandas as pd


my_data_set = {'cars' : ["BMW", "FORD", "VOLVO"],
               'passing' : [3, 7, 2]
}

m = pd.DataFrame(my_data_set)
print(m)

#kodun çıktısı:
'''
    cars  passing
0    BMW        3
1   FORD        7
2  VOLVO        2
'''