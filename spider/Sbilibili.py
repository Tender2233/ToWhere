import time

import pymysql
import requests


def getBilibili():
    url = 'https://www.anyknew.com/api/v1/sites/bilibili'
    r = requests.get(url)
    if r.status_code == 200:
        conn = pymysql.connect(host='cdb-r9tzcdd0.cd.tencentcdb.com',
                               port=10125,
                               user='root',
                               passwd="tenderkun123",
                               db='towhere')

        pop_data = r.json()
        date = time.localtime(time.time())
        sqldate = time.strftime("%Y-%m-%d %X", date)
        items = pop_data['data']['site']["subs"][0]['items']
        rank = 1
        for item in items:
            print(item)
            cur = conn.cursor()
            sql = "insert into rank_bilibili(iid,title,add_date,get_date,rank) values('%d','%s','%d','%s','%d')"
            data = (item['iid'], item['title'], item['add_date'], sqldate, rank)
            cur.execute(sql % data)
            rank += 1
            conn.commit()


if __name__ == '__main__':
    print('get once')
    getBilibili()
