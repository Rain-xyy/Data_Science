import pandas as pd

path_tf = 'filter_data/one_fifth/one_fifth_tf_values_2020.3.10-2020.6.15.xlsx'
path_idf = 'filter_data/idf_values.xlsx'
df_tf=pd.read_excel(path_tf)
df_idf=pd.read_excel(path_idf)

tf_words=df_tf['word'].tolist()
tf_value=df_tf['tf_value'].tolist()
idf_words=df_idf['word'].tolist()
idf_value=df_idf['idf_value'].tolist()

tf_dic=dict(zip(tf_words,tf_value))
idf_dic=dict(zip(idf_words,idf_value))

dict_tfidf={}
for i in tf_dic.keys():
    dict_tfidf[i]=tf_dic[i]*idf_dic[i]
#tfidf_order=sorted(dict_tfidf.items(),key=lambda x:x[1],reverse=True)

tfidf=pd.DataFrame(pd.Series(dict_tfidf),columns=['tfidf_value'])
tfidf=tfidf.reset_index().rename(columns={'index':'word'})
tfidf = tfidf.sort_values(by='tfidf_value', ascending=False)
tfidf.to_excel('filter_data/one_fifth/tf_idf_2020.3.10-2020.6.15.xlsx')
print(tfidf)
