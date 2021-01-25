# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 16:53
# @Author  : 夏宇
# @FileName: getCommentThirdStage.py
# @Software: PyCharm

import pandas as pd
import requests
import re
import time

headers = {
        'Cookie': '_T_WM=91415639404; WEIBOCN_FROM=1110006030; SUB=_2A25NDqSsDeRhGeFM61AS9y7NwziIHXVu8MzkrDV6PUJbktANLWjGkW1NQOcY1hd1_czyIC-v0WHpfPnKpZonU5Z4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW2Jis_vnJLuQ9.RymcddHl5NHD95QNeo5Ee0M7eKnXWs4DqcjDi--fi-2Xi-zXi--fiKysi-zNi--ciKnci-2Ri--ciKnci-2RIJ80dcRt; SSOLoginState=1611322620; MLOGIN=1; XSRF-TOKEN=9fab55; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000061%26fid%3D4596282175553130%26oid%3D4596282175553130',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'X-Requested-With': 'XMLHttpRequest'
    }

frompath = '2020.2.10-2020.2.13.xlsx'
topath = 'Comments2020.2.10-2.13.xlsx'

df = pd.read_excel(frompath)
url_list = df['文章url'].tolist()
id_list = df['文章id'].tolist()
comments_count = df['评论量'].tolist()
like_count = df['点赞量'].tolist()
time_list = df['发布时间'].tolist()

title_list = []
comment_list = []
like_list = []
publish_time = []
numOfComment = []

def run():
    for i in range(0,len(url_list)):
        try:
            print(i)
            url = url_list[i]
            response = requests.get(url, headers = headers)
            if (response.status_code != 200):
                print('ResponseError!')
                break
            time.sleep(2)
            html = response.text
            title = re.findall(r"\"status_title\": \"(.*)\"", html)[0]
            content = re.findall("\"text\":(.*)", html)[0]
            if(filter(title, content)):
                getComment(id_list[i])
                title_list.append(title)
                like_list.append(like_count[i])
                publish_time.append(time_list[i])
                numOfComment.append(comments_count[i])
            else:
                pass
        except:
            print(url)
            print('error')
    data = {'title':title_list, 'time':publish_time, 'like':like_list, 'comment_count':numOfComment, 'comment':comment_list}
    dataDF = pd.DataFrame(data)
    dataDF.to_excel(topath)

def filter(title, content):
    if(title.__contains__("疫情") or title.__contains__("疫") or title.__contains__('新型肺炎') or title.__contains__('封城') or title.__contains__('医')
        or title.__contains__('隔离') or title.__contains__('传染') or title.__contains__('潜伏期') or title.__contains__('14天') or title.__contains__('口罩')
        or title.__contains__("新型冠状") or title.__contains__('Covid-19') or title.__contains__('COVID-19') or title.__contains__('李文亮') or title.__contains__('钟南山')
        or title.__contains__('李兰娟')):
        return True
    elif (content.__contains__("疫情") or content.__contains__("疫") or content.__contains__('新型肺炎') or content.__contains__(
            '封城') or content.__contains__('医')
            or content.__contains__('隔离') or content.__contains__('传染') or content.__contains__(
                '潜伏期') or content.__contains__('14天') or content.__contains__('口罩')
            or content.__contains__("新型冠状") or content.__contains__('Covid-19') or content.__contains__(
                'COVID-19') or content.__contains__('李文亮') or content.__contains__('钟南山')
            or content.__contains__('李兰娟')):
        return True
    else:
        return False

def getComment(id):
    comment = []
    url = 'https://m.weibo.cn/comments/hotflow?id=' + str(id) + '&mid=' + str(id) + '&max_id_type=0'
    response = requests.get(url, headers = headers)
    json_data = response.json()
    data = json_data.get('data').get('data')
    for i in range(0,10):
        text = re.sub("[A-Za-z0-9]", "", data[i]['text'])
        comment.append(text)
    print(len(comment))
    comment_list.append(comment)


if __name__=="__main__":
    run()