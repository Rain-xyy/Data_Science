import pandas as pd
path = 'filter_data/stage_4_emotion_dict.xlsx'
df = pd.read_excel(path)
frequency=df['frequency'].tolist()
total_word_count=sum(frequency)
percent=[]
for i in frequency:
    percent.append(i/total_word_count)
df['percent']=percent
df.to_excel('filter_data/stage_4_emotion_dict.xlsx')