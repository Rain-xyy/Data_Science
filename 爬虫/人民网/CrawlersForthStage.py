# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 11:56
# @Author  : 夏宇
# @FileName: CrawlersForthStage.py
# @Software: PyCharm

import requests
import time
import pandas as pd

headers = {
        'Cookie': '_T_WM=46000520627; SCF=AvJaTz_zp1Mon-EoUwc1elVgjJebLBZ1TAzuFR8MoJSN5s7zkrGgek_ivYFwj1gRiIl5qMu8fSHXuFGjLtfgO8Q.; SUB=_2A25NDdVuDeRhGeNM71MR-S_IyjyIHXVu8fsmrDV6PUJbktAfLWHkkW1NTjQyCJwaOSaBKOtpY1WxtsS7Po0AEnjG; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W54ubMqwyiINaGaSbVHYhbu5NHD95QfeoBpeh.pSh27Ws4Dqcj.i--fiKnpi-zci--ciK.Ri-8si--4i-zRi-82i--Ni-iWi-zR; MLOGIN=1; WEIBOCN_FROM=1110106030; XSRF-TOKEN=5a3291; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E4%25BA%25BA%25E6%25B0%2591%25E6%2597%25A5%25E6%258A%25A5%26fid%3D1005052803301701%26uicode%3D10000011',
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
    path = '2020.3.10-2020.6.15.xlsx'
    #1875-2070; 2020.3.10-6.15
    for page in range(1160,1811):
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
    for i in range(0, len(cards)):
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