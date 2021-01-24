from pyhanlp import *
import pandas as pd

HanLP.Config.ShowTermNature = False
segment = DoubleArrayTrieSegment()
segment.enablePartOfSpeechTagging(True)

def main():
    # HanLP.Config.enableDebug()
    #  为了避免你等得无聊，开启调试模式说点什么:-)
    path = '分时段/3.10-2020.6.15_total.xlsx'
    df = pd.read_excel(path)
    comment_list = df['comment'].tolist()
    comment_list = reversed(comment_list)
    # Toprint=comment_list[7]
    # text=segment.seg(Toprint)
    dic = load_file('stopwords.txt')
    # result=remove_stop_word(text,dic)
    # print(result)
    k = 0
    total_result_of_a_file = []
    for i in comment_list:
        print(k)
        k += 1
        # text = segment.seg(i)
        text=HanLP.segment(i)
        result = remove_stop_word(text, dic)
        print(result)
        total_result_of_a_file.append(result)
        print()

    for i in total_result_of_a_file:
        str_to_write = ' '.join(i)
        # str_to_write=str_to_write.encode('utf-8')
        with open('分时段/stage_4_words.txt', 'a', encoding='utf-8') as f:
            # try:
            f.write(str_to_write)
            f.write('\n')
            # except:
            # pass
        f.close()


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.readlines()
    f.close()
    result = []
    for content in contents:
        result.append(content.strip())
    result.append(' ')
    result.append('[')
    result.append(']')
    result.append("'")
    result.append('/')
    result.append('  ')
    return result


def remove_stop_word(text, dic):
    result = []
    for k in text:
        try:
            if k.word not in dic:
                result.append(k.word)
        except:
            pass
    symbol = [',', '.', ':', ';', '{', '}', '[', ']', '|', '～', '"', '-', '+', '=', '_', "'", '/', '……', '%', ' ', '#','^',"\\"]
    result_new = []
    flag = 1
    for i in result:
        flag = 1
        for j in symbol:
            if j in i:
                flag = 0
                break
        if flag == 1:
            result_new.append(i)

    return result_new


if __name__ == '__main__':
    main()
