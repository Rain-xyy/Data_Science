# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:35:29 2021

@author: DELL
"""
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import pandas as pd

words=[]
df=pd.read_excel("D://one_fifth_tf_values_2020.3.10-2020.6.15.xlsx")#更改数据即可绘制另外三个时期的tf词云
df=df.reset_index(drop=True)
word=df["word"]
tf_value=df["tf_value"]
for i in range(0,100):
    lst=[]
    lst.append(word[i])
    lst+=[tf_value[i]]
    words.append(tuple(lst))

c = (
    WordCloud()
    .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
    .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-shape-diamond"))
    .render("wordcloud_diamond.html")
)