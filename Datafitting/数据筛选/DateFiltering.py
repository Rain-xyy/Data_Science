import pandas as pd

def filter(path, lowerBound):
    df = pd.read_excel(path)
    title_list = df['title'].tolist()
    time_list = df['time'].tolist()
    like_count_list = df['like'].tolist()
    comment_count_list = df['comment_count'].tolist()
    comment_list = df['comment'].tolist()
    del_list = []
    for i in range(0, len(comment_count_list)):
        if(comment_count_list[i] >= lowerBound):
            pass
        else:
            del_list.append(i)
    for value in reversed(del_list):
        del title_list[value]
        del time_list[value]
        del comment_count_list[value]
        del comment_list[value]
        del like_count_list[value]
    data = {'title': title_list, 'time': time_list, 'like': like_count_list, 'comment_count': comment_count_list, 'comment': comment_list}
    new_df = pd.DataFrame(data)
    new_df.to_excel('filter_data_' + path)

filter('1_2019.12.8-2020.1.23_Comments.xlsx', 804)
filter('2_2020.1.23-2020.2.7_Comments.xlsx', 736)
filter('3_2020.2.10-2020.2.13_Comments.xlsx', 709)
filter('4_2020.3.10-2020.6.15_Comments.xlsx', 536)