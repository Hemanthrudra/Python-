
# Pandas

# pandas.DataFrame(data,index,colums,dtype,copy)

# Importing the pandas library and aliasing as pd

import pandas as pd
# df=pd.DataFrame()
# print(df)

# data=[1,2,3,4,5]
# df=pd.DataFrame(data)
# print(df)

# data=[['Alex',10],['Bob',12],['Clarke',13]]
# df=pd.DataFrame(data,columns=['Name','Age'],dtype=float)
# print(df)

# data=[['Alex',10],['Bob',12],['Clarke',13]]
# df=pd.DataFrame(data,columns=['Name','Age'])
# print(df)

# Create a dataframe from Dic of ndarrays/lists

# data={'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,3,29,42]}
# df=pd.DataFrame(data)
# print(df)


# data={'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,29,42]}
# df=pd.DataFrame(data,index=['rank1','rank2','rank3','rank4'])
# print(df)

# data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
# df=pd.DataFrame(data)
# print(df)

# data=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
# df=pd.DataFrame(data,index=['first','second'])
# print(df)

# data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
# df1=pd.DataFrame(data,index=['first','second'],columns=['a','b'])
# df2=pd.DataFrame(data,index=['first','second'],columns=['a','b1'])
# print(df1)
# print(df2)

# d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print(df)

# d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print(df['one'])

# d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# # adding a new column to an existing Dataframe object with column label by passing new series
# print(df)
# print('Adding a new column by passing as series:')
# print(df)
# df['three']=pd.Series([10,20,30],index=['a','b','c'])
# print("Adding a new column using the existing column in DataFrame:")
# df['four']=df['one']+df['three']
# print(df)
#
# d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print("our dataframe is:")
# print(df)
# # Uing del function
# print('Deleting the first column using DEL function:')
# del df['one']
# print(df)
# # Using pop Function
# print("Deleting another column using pop function:")
# df.pop('two')
# print(df)

# Row selection

# d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print(df.loc['b'])
#
# # Selection by integer location
#
# d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print(df.iloc[2])
#
# # Slice Rows
# d={'one':pd.Series([1,2,3],index=['a','b','c']),'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df=pd.DataFrame(d)
# print(df[2:4])

# Addition of rows

# df=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
# df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
# df=df.append(df2)
# print(df)

# Deletion of Rows

df=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2=pd.DataFrame([[5,6],[7,8]],columns=['a','b'])
df=df.append(df2)
# Drop rows with label 0
df=df.drop(0)
print(df)