# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:49:37 2021

@author: DELL
"""

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
def plot(path):
    df=pd.read_excel(path)
    list_comment_counts=df["comment_count"]
    def lessThan8000(x):
        return  x < 8000
    listFiltered=list(filter(lessThan8000,list_comment_counts))
    listFiltered.sort()
    
    #函数：
    #使用矩估计法（点估计）估计高斯分布的u和v
    def parameter(final_listY,n):
        sum0=0
        for i in range(0,len(final_listY)):
            sum0+=(i+1)*final_listY[i]
        u=sum0/sum(final_listY)
        v=0
        for i in range(0,len(final_listY)):
            for j in range(0,final_listY[i]):
                v+=((i+1)-u)**2
        v/=sum(final_listY)-1
        v=math.sqrt(v)
        return u,v
        
    #prepareDataXY(listFiltered)
    lsty=[]
    n=(int) (max(listFiltered)/1) +1
    for i in range(0,n):
        m=max(listFiltered)/n+1
        lsty+=[len(list(filter(lambda x:i*m<x<=(i+1)*m,listFiltered)))]
    lstx=[]
    for i in range(0,n):
        #横坐标
        lstx+=[(i+1)]#横坐标单位:...
        
    u,v=parameter(lsty,n)  
     
    #高斯分布函数,需要使用numpy
    def func(x, u, v):
        a=np.sqrt(2*np.pi)*v
        b=1/a
        c=-np.square(x-u)/(2*np.square(v))
        d=np.exp(c)
        return b*d
    
    xdata=np.array(lstx)
    ydata =np.array(lsty)
    #第一张图，文章的大致分布： 结论为大部分文章在两三千条评论
    plt.plot(xdata,ydata,'b-')
    plt.title('2020.1.23-2020.2.7')
    
    #err_stdev = 0.2
    #生成均值为0，标准差为err_stdev为0.2的高斯噪声
    #y_noise = err_stdev * np.random.normal(size=xdata.size)
    y = func(xdata, u,v)
    ydata = y 
    
    plt.figure('拟合图')
    plt.plot(xdata, ydata, 'b-', label='data')
    
    popt, pcov = curve_fit(func, xdata, ydata)
#    a = popt[0] 
#    b = popt[1]
    #预测值
    y_pred = [func(i, popt[0],popt[1]) for i in xdata]
    #画图
    plt.plot(xdata,y_pred,'r--')
    plt.title('2020.1.23-2020.2.7')
    plt.xlabel('Comment Number')
    plt.ylabel('Proportion of Article')
    print(popt)
    from sklearn.metrics import r2_score
    r2 = r2_score(ydata , y_pred )
    print('高斯函数拟合R方为:',r2)
    
plot('D:\\2_2020.1.23-2020.2.7_Comments.xlsx')
    
