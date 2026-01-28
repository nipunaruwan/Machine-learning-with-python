#   1.pandas


# import pandas as pd
#
# list =['a','b','c','d','e']
#
# expample_series = pd.Series(list ,index=['letter1','letter2','letter3','letter4','letter5'])
# print(expample_series)
#
# print(expample_series['letter4'])


#   2.Data_Frame

# import  pandas as pd
#
#
# data = {'Name':['jal','princi','Gavruv','anju'],
#         'Age':[27,24,22,32],
#         'Address':['Delhi','kanpur','Allahabad','kannauj'],
#         'Qualification':['Msc','MA','MCA','phd']
#        }
#
#
# df = pd.DataFrame(data)
# print(df)
# print(df['Name'][3])
# print(df['Address'][2])
# print(df['Qualification'][1])


# 03.selecting specific Raws and colums of a Dataframe


#
# import  pandas as pd
#
#
# data = {'Name':['jal','princi','Gavruv','anju'],
#         'Age':[27,24,22,32],
#         'Address':['Delhi','kanpur','Allahabad','kannauj'],
#         'Qualification':['Msc','MA','MCA','phd']
#        }
#
#
# df = pd.DataFrame(data)
# print(df)
# # print(df['Name'])
# # print(df[['Name']])
#
# print(df.loc[1])  #return pandas serius   1d array
# # print(df.loc[[1]])  #return data frame  2d array
#



# 04.Selecting rows by column values





# 05.Iterating Columns in a Dataframe

import  pandas as pd


data = {'Name':['jal','princi','Gavruv','anju'],
        'Age':[27,24,22,32],
        'Address':['Delhi','kanpur','Allahabad','kannauj'],
        'Qualification':['Msc','MA','MCA','phd']
       }


df = pd.DataFrame(data)
print(df)

for i in df.index:
    print(df.Address[i])