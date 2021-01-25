# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:45:50 2021

@author: DELL
"""
import pandas as pd
import numpy as np
import math
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def plot(path,p):
    df=pd.read_excel(path)
    list_comment_counts=df["comment_count"]
    def lessThan8000(x):
        return  x < 8000
    listFiltered=list(filter(lessThan8000,list_comment_counts))
    listFiltered.sort()
    
    #函数：
    #使用矩估计法（点估计）估计高斯分布的u和v，只将相同的数压缩
    #final_listY表示0-10评论数的文章有几篇 10-20有几篇等等：
    #0-10用1表示 10-20用2表示以此类推  1，2...作为随机变量X  单位为：10条评论
    #final_listY中0处对应的值是样本中落在X=1  1处落在X=2...依此类推
    def parameter(final_listY,n):
        sum0=0
        for i in range(0,len(final_listY)):
            sum0+=(i+1)*final_listY[i]
        u=sum0/sum(final_listY)
        v=0
        for i in range(0,len(final_listY)):
            for j in range(0,final_listY[i]):
                v+=((i+(i+1))/2-u)**2
        v/=sum(final_listY)-1
        v=math.sqrt(v)
        return u,v
    
    #prepareDataXY(listFiltered) 统计样本落入随机变量X的情况
    lsty=[]
    n=0
    if max(listFiltered)%p!=0:
        n=(int) (max(listFiltered)/p) +1
    else:
        n=(int) (max(listFiltered)/p)
    for i in range(0,n):
        lsty+=[len(list(filter(lambda x:i*p<x<=(i+1)*p,listFiltered)))]
    lstx=[]
    for i in range(0,n):
        #横坐标(ip,(i+1)*p]条评论
        lstx+=[(i+1)]
        
    xdata=np.array(lstx)
    ydata =np.array(lsty)
    #文章的大致分布： 结论为大部分文章在两三千条评论
    plt.plot(xdata,ydata,'b-')
    plt.title('2019.12.8-2020.1.23')
    
    #高斯分布函数模型,需要使用numpy！
    def func(x, u, v):
        a=np.sqrt(2*np.pi)*v
        b=1/a
        c=-np.square(x-u)/(2*np.square(v))
        d=np.exp(c)
        return b*d
    
    #一、调用函数计算u、v
    u,v=parameter(lsty,n)  
    
    #二、设置噪声
    #err_stdev = 0.001
    #生成均值为0，标准差为err_stdev为0.001的高斯噪声
    #y_noise = err_stdev * np.random.normal(size=xdata.size)
    y = func(xdata, u,v)
    ydata = y 
    
    plt.figure('拟合图')
    plt.plot(xdata, ydata, 'b-', label='data')
    popt, pcov = curve_fit(func, xdata, ydata)
    #a = popt[0] 
    #b = popt[1]
    #预测值
    y_pred = [func(i, popt[0],popt[1]) for i in xdata]
    #画图
    plt.plot(xdata,y_pred,'r--')
    plt.title('2019.12.8-2020.1.23')
    plt.xlabel('Comment Number')
    plt.ylabel('Proportion of Article')
    print(popt)
    from sklearn.metrics import r2_score
    r2 = r2_score(ydata , y_pred)
    print('高斯函数拟合R方为:',r2)
    
plot('D:\\1_2019.12.8-2020.1.23_Comments.xlsx',100)

