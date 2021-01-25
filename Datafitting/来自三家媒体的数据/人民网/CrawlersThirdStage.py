# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 11:51
# @Author  : 夏宇
# @FileName: CrawlersThirdStage.py
# @Software: PyCharm

import requests
import time
import pandas as pd

headers = {
        'Cookie': '_T_WM=91415639404; WEIBOCN_FROM=1110006030; SUB=_2A25NDqSsDeRhGeFM61AS9y7NwziIHXVu8MzkrDV6PUJbktANLWjGkW1NQOcY1hd1_czyIC-v0WHpfPnKpZonU5Z4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW2Jis_vnJLuQ9.RymcddHl5NHD95QNeo5Ee0M7eKnXWs4DqcjDi--fi-2Xi-zXi--fiKysi-zNi--ciKnci-2Ri--ciKnci-2RIJ80dcRt; SSOLoginState=1611322620; MLOGIN=1; XSRF-TOKEN=9fab55; M_WEIBOCN_PARAMS=lfid%3D102803%26luicode%3D20000174%26uicode%3D20000061%26fid%3D4596282175553130%26oid%3D4596282175553130',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
        'X-Requested-With': 'XMLHttpRequest'
    }
#记录文章url
url_list = []
#记录文章id
id_list = []
#记录发表时间
time_list = []
#记录转发量
reposts_count_list = []
#记录点赞量
attitudes_count_list = []
#记录评论量
comments_count_list = []


def run():
    PageURL = 'https://m.weibo.cn/api/container/getIndex?containerid=2304132286908003_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=2310022286908003_-_HOTMBLOG&page_type=03&page='
    path = '2020.2.10-2020.2.13.xlsx'
    #1875-2070; 2020.2.10-2.13
    for page in range(2040,2076):
        print(page)
        json_data = get_page(PageURL + str(page))
        time.sleep(1)
        write_info(json_data)


    data = {'文章url': url_list, '文章id': id_list, '转发量':reposts_count_list, "点赞量":attitudes_count_list, '评论量':comments_count_list, '发布时间':time_list}
    #print(len(url_list), len(id_list), len(reposts_count_list), len(attitudes_count_list), len(comments_count_list))
    dataDF = pd.DataFrame(data)
    dataDF.to_excel(path)


def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get('data')
    except requests.ConnectionError as e:
        print('error', e.args)

def write_info(data):
    try:
        cards = data.get('cards')
    except:
        print('error')
        time.sleep(3)
        return
    for i in range(0,len(cards)):
        items = cards[i]
        try:
            id_list.append(items['mblog']['id'])
            time_list.append(items['mblog']['created_at'])
            reposts_count_list.append(items['mblog']['reposts_count'])
            attitudes_count_list.append(items['mblog']['attitudes_count'])
            comments_count_list.append(items['mblog']['comments_count'])
            url_list.append(items.get('scheme'))
        except:
            pass

if __name__ == "__main__":
    run()