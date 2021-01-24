from collections import defaultdict
import pandas as pd


def read_and_split():
    comment_list = []
    with open('filter_data/filter_data_4_comments.txt', 'r', encoding='utf-8') as f:
        string_for_lines = f.readlines()
        f.close()
    #for i in string_for_lines:
    #    list_for_one_line = i.split(' ')
     #   if list_for_one_line[-1][-1] == '\n':
      #      list_for_one_line[-1] = list_for_one_line[-1][:-1]
       # comment_list.append(list_for_one_line)
    for i in range(0,len(string_for_lines),5):
        list_for_one_line=string_for_lines[i].split(' ')
        if list_for_one_line[-1][-1] == '\n':
          list_for_one_line[-1] = list_for_one_line[-1][:-1]
        comment_list.append(list_for_one_line)

    return comment_list


def word_tf_value(list_words):
    doc_frequency = defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i] += 1

    word_tf = {}
    word_count = sum(doc_frequency.values())
    for i in doc_frequency:
        word_tf[i] = doc_frequency[i] / word_count
    return word_tf


def main():
    total_comment_of_a_file = read_and_split()
    # total_return_list=[]
    # for i in total_comment_of_a_file:
    # total_return_list=total_return_list+i
    # word_tf={}
    word_tf = word_tf_value(total_comment_of_a_file)
    dict=pd.DataFrame(pd.Series(word_tf),columns=['tf_value'])
    dict=dict.reset_index().rename(columns={'index':'word'})
    dict=dict.sort_values(by='tf_value',ascending=False)
    dict.to_excel('filter_data/one_fifth_tf_values_2020.3.10-2020.6.15.xlsx')
    print(dict)


if __name__ == '__main__':
    main()
