# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:53:25 2021

@author: DELL
"""
#合并
import pandas as pd
import os

result =[]
def get_all(path):   # 递归获取指定目录下所有文件的绝对路径（非目录）
    dir_list = os.listdir(path)
    for i in dir_list:
        sub_dir = os.path.join(path, i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:   # 此时sub_dir是文件的绝对路径
            if "Comments" in sub_dir:
                result.append(sub_dir)
    
get_all('C://Users//DELL//Desktop//数据科学大作业//LargeWork')
df1=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
df4=pd.DataFrame()
for i in result:
    if '2019.12.8-2020.1.23' in i:
        df1=df1.append(pd.read_excel(i))
    if '2020.1.23-2020.2.7' in i:
        df2=df2.append(pd.read_excel(i))
    if '2020.2.10-2.13' in i:
        df3=df3.append(pd.read_excel(i))
    if '2020.3.10-2020.6.15' in i:
        df4=df4.append(pd.read_excel(i))
df1.to_excel("D://1_2019.12.8-2020.1.23_Comments.xlsx")
df2.to_excel("D://2_2020.1.23-2020.2.7_Comments.xlsx")
df3.to_excel("D://3_2020.2.10-2.13_Comments.xlsx")
df4.to_excel("D://4_2020.3.10-2020.6.15_Comments.xlsx")
