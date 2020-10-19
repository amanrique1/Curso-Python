import pandas as pd
import numpy as np
from collections import Counter

df = pd.read_csv("Colombia_COVID19_Coronavirus_casos_diarios.csv")
#head and tail are for the 5 first and last registers
print(df.head())
print(df.tail())
print(df.columns)
#Check the number of nulls for each column
print(df.isnull().sum())
print("-------------------------------------------")
print("Total casos: "+str(df["NUEVOS_CASOS"].sum()))
#Define the rules for 'null' cases, nan can also be used for non numeric fields
df.loc[df.NUEVOS_CASOS == 0, 'NUEVOS_CASOS'] = np.nan
print(df.isnull().sum())
#isna tells if the field is null
print(df.isna())
print("Length Before:", len(df))
#dropna removes the missing values, when inplace is True it refresh df but when it's false or empty you need to reassing the variable
dft=df.dropna()
print("Length After:", len(dft))
#fillna init  the null value  with given value and inplace says if it's the value is in the same variable or we need to reassign it
df.fillna(0, inplace=True)
print(df.isnull().sum())
emptyDays = df[df['NUEVOS_CASOS'] == 0]
print(emptyDays.head())
#we can also accumulate conditions
happyDays = df[(df.NUEVOS_CASOS == 0) & (df.NUEVOS_MUERTOS == 0)]
#Filtering data the indexes keep the same as when we load the file so with reset indexes we reassign it
emptyDays.reset_index(inplace=True)
del emptyDays['index']
print(emptyDays.head())
#iloc is used to get the  specific row
print(df.iloc[0])
#loc is used to get column data, you can get many at the same time
print(df.loc[0:3, 'NUEVOS_CASOS'])
"""
There are many usefull math functions such as:
*.mean()
*.max()
*.min()
*.count()
*.std() //for standard deviation
*.groupby() //you can combine it with other functions and many columns
************How many male/female smokes*****************
df_yes = df[df['smoker'] == 'yes']
df_yes  = df_yes.groupby(['sex'])['smoker'].count()
df  = df.groupby(['smoker', 'sex'])['charges'].mean()
"""
for index, rows in df.iterrows():
    print("Index: ",index, "Nuevos Casos: ", rows['NUEVOS_CASOS'])
    #at is used to create new columns
    if(rows['NUEVOS_CASOS']==0) and (rows['TOTAL_MUERTES']==0):
        df.at[index, 'CLEAN_DAY'] = True
    else:
        df.at[index, 'CLEAN_DAY'] = False
print(df.head())
#Let's print how many reports do we have for each date
print(Counter(df['FECHA_ACTUALIZACION']))

#----------------------------More efficient methods--------------------------
#.eval() helps us to make quick operations more efficiently
print(df.eval('ACTIVE_SICKS = TOTAL_CASOS - TOTAL_RECUPERADOS - TOTAL_MUERTES'))
#query is another way that we can use to filter the data
happyDays=df.query('NUEVOS_CASOS == 0 and TOTAL_MUERTES == 0')

#Return the data with our changes to a csv
df.to_csv("Colombia_COVID19_Coronavirus_casos_diarios_mod.csv")
#Testing
df2 = df.copy()
df2.NUEVOS_CASOS = df2.NUEVOS_CASOS.astype('int')
pd.testing.assert_frame_equal(df, df2)