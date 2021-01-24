from collections import defaultdict
import pandas as pd
import math


def read_and_split():
    comment_list = []
    with open('total_comments.txt', 'r', encoding='utf-8',errors='ignore') as f:
        string_for_lines = f.readlines()
        print("readline complete")
        f.close()
    for i in string_for_lines:
        list_for_one_line = i.split(' ')
        if list_for_one_line[-1][-1] == '\n':
            list_for_one_line[-1] = list_for_one_line[-1][:-1]
        comment_list.append(list_for_one_line)
    print('comment_list constructed')
    return comment_list


def word_idf_value(list_words):
    print('enter idf calculation')
    doc_frequency = defaultdict(int)
    for word_list in list_words:
        for i in word_list:
            doc_frequency[i] += 1

    print('doc frequency completed')
    doc_num=len(list_words)
    word_idf={}
    word_doc=defaultdict(int)
    n=0
    for i in doc_frequency:
        for j in list_words:
            print(n)
            n+=1
            if i in j:
                word_doc[i]+=1
    print('word_doc completed')
    k=0
    for i in doc_frequency:
        word_idf[i]=math.log(doc_num/(word_doc[i]+1))
        print(k)
        k+=1
    return word_idf


def main():
    total_comment_of_a_file = read_and_split()
    word_idf = word_idf_value(total_comment_of_a_file)
    dict = pd.DataFrame(pd.Series(word_idf), columns=['idf_value'])
    dict = dict.reset_index().rename(columns={'index':'word'})
    dict = dict.sort_values(by='idf_value', ascending=False)
    dict.to_excel('idf_values.xlsx')
    print(dict)


if __name__ == '__main__':
    main()
