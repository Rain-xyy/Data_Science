# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 13:57
# @Author  : 夏宇
# @FileName: CrawlersFirstStage.py
# @Software: PyCharm

import requests
import time
import pandas as pd

headers = {
        'Cookie': 'SUB=_2A25NAsYTDeRhGeFM4lMU8C_JzzWIHXVuDOpbrDV6PUJbktANLWPNkW1NQIo-5Qk-nB30gx_215TDePSe8V0IjK8p; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhyTJB9eGbhVdODe702Yr5A5NHD95QNeo.pSK5pSKB4Ws4Dqc_pi--ciKLhi-8hi--ciK.Ri-8si--ciK.Ni-27i--ciKn0iKnfi--Xi-iWi-iWi--fi-2fiKnRi--Xi-i2iK.fi--Xi-iFiK.4i--fi-82iK.7i--RiK.7i-i2i--fiKnNi-2pi--fi-z7iK.R1K-feKMt; _T_WM=59612560283; WEIBOCN_FROM=1110006030; MLOGIN=1; XSRF-TOKEN=d7d024; M_WEIBOCN_PARAMS=oid%3D4595416693740070%26luicode%3D20000061%26lfid%3D4595416693740070',
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
    PageURL = 'https://m.weibo.cn/api/container/getIndex?containerid=2304132656274875_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=2310022656274875_-_HOTMBLOG&page_type=03&page='
    path = '2019.12.8-2020.1.23.xlsx'
    for page in range(1920,2094):
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