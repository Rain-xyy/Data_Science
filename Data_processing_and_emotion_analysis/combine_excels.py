import pandas as pd
path1 = '分时段/3.10-2020.6.15_total.xlsx'
path2 = '分时段/2020.2.10-2.13_total.xlsx'
path3= '分时段/Comments2019.12.8-2020.1.23_total.xlsx'
path4='分时段/Comments2020.1.23-2020.2.7_total.xlsx'

df1=pd.read_excel(path1)
df2=pd.read_excel(path2)
df3=pd.read_excel(path3)
df4=pd.read_excel(path4)
newlist=[]
newlist.append(df1)
newlist.append(df2)
newlist.append(df3)
newlist.append(df4)
df5=pd.concat(newlist)
df5.to_excel('分时段/total_comments.xlsx',encoding='utf-8',index=False)
print(df5)