import pandas as pd
from collections import defaultdict


def init_emotion_dict():
    dict = {'气死': '愤怒', '医闹': '愤怒', '医患': '愤怒', '大理': '愤怒', '骂': '愤怒', '怒': '愤怒', '发国难财': '愤怒',
            '举报': '愤怒','气死我了': '愤怒', '他妈': '愤怒','害怕': '恐慌', '恐慌': '恐慌', '可怕': '恐慌', '逃离': '恐慌',
            '严重性': '恐慌', '悲剧重演': '恐慌', '急': '恐慌', '买不到': '恐慌','封省': '恐慌', '紧缺': '恐慌',
            '怕': '恐慌', '双黄连': '恐慌', '告急': '恐慌', '不够': '恐慌', '难关': '恐慌','伤': '伤心', '伤害': '伤心',
            '走好': '伤心', '悲': '伤心', '失望': '伤心', '绝望': '伤心', '委屈': '伤心', '寒心': '伤心', '伤心': '伤心',
            '悲伤': '伤心', '可怜': '伤心', '心疼': '伤心', '太难': '伤心','为什么': '怀疑', '不信': '怀疑', '费解': '怀疑',
            '怎么办': '怀疑', '疑问': '怀疑', '是不是': '怀疑','微笑': '高兴', '赞': '高兴', '微好消息': '高兴',
            '打败': '高兴', '太好了': '高兴', '治愈': '高兴', '嘻嘻': '高兴', '开心': '高兴', '笑': '高兴',
            '成功': '高兴', '太棒': '高兴', '喜欢': '高兴', '哈哈哈': '高兴', '解封': '高兴', '清零': '高兴', '幸福': '高兴',
            '棒': '高兴', '快乐': '高兴','笑哈哈': '高兴', '温暖': '高兴','致敬': '崇敬', '辛苦': '崇敬', '谢谢': '崇敬',
            '理解': '崇敬', '感谢': '崇敬', '尊重': '崇敬', '英雄': '崇敬', '牛逼': '崇敬', '伟大': '崇敬','骄傲': '崇敬',
            '鼓掌': '崇敬', '感恩': '崇敬', '逆行': '崇敬', '白衣天使': '崇敬', '感动': '崇敬', '缅怀': '崇敬', '铭记': '崇敬',
            '希望': '希望', '平安': '希望', '相信': '希望', '': '希望', '挺住': '希望', '加油': '希望', '平平安安': '希望',
            '健康': '希望', '战胜': '希望','众志成城': '希望', '早日康复': '希望', '万众一心': '希望', '祝福': '希望',
            '期待': '希望', '憧憬': '希望', '奋斗': '希望'}
    return dict


def read_and_split():
    comment_list=[]
    path='分时段/stage_4_words.txt'
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
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


def search(comment_list, dic):
    n=0
    emotion_frequency = defaultdict(int)
    for i in comment_list:
        print(n)
        n+=1
        for j in i:
            if j in dic.keys():
                emotion_frequency[dic[j]] += 1
    return emotion_frequency


def main():
    emotion_dict = init_emotion_dict()
    comment_list = read_and_split()
    emotion_frequency = search(comment_list, emotion_dict)
    dic_emotion=pd.DataFrame(pd.Series(emotion_frequency),columns=['frequency'])
    dic_emotion=dic_emotion.reset_index().rename(columns={'index':'emotion'})
    dic_emotion=dic_emotion.sort_values(by='frequency',ascending=False)
    dic_emotion.to_excel('分时段/stage_4_emotion_dict.xlsx',encoding='utf-8')
    print(dic_emotion)


if __name__ == '__main__':
    main()