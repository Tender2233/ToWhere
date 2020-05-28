import time

import pymysql
import requests


def getZhihu():
    url = 'https://www.anyknew.com/api/v1/sites/zhihu'
    r = requests.get(url)
    if r.status_code == 200:
        conn = pymysql.connect(host='cdb-r9tzcdd0.cd.tencentcdb.com',
                               port=10125,
                               user='root',
                               passwd="tenderkun123",
                               db='towhere')
        date = time.localtime(time.time())
        sqldate = time.strftime("%Y-%m-%d %X", date)
        pop_data = r.json()
        items = pop_data['data']['site']["subs"][0]['items']
        words = pop_data['data']['site']["subs"][1]['items']
        rank = 1
        for item in items:
            print(item)
            cur = conn.cursor()
            sql = "insert into rank_zhihu(iid,title,add_date,get_date,rank) values('%d','%s','%d','%s','%d')"
            data = (item['iid'], item['title'], item['add_date'], sqldate, rank)
            # print(sql % data)
            cur.execute(sql % data)
            rank += 1
            conn.commit()
        rank = 1
        for word in words:
            print(word)
            cur = conn.cursor()
            sql = "insert into word_zhihu(iid,title,add_date,get_date,rank) values('%d','%s','%d','%s','%d')"
            data = (word['iid'], word['title'], word['add_date'], sqldate, rank)
            # print(sql % data)
            cur.execute(sql % data)
            rank += 1
            conn.commit()


if __name__ == '__main__':
    print('get once')
    getZhihu()
