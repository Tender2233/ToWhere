import time

import pymysql
import requests


def getBaidu():
    url = 'https://www.anyknew.com/api/v1/sites/baidu'
    r = requests.get(url)
    if r.status_code == 200:
        conn = pymysql.connect(host='cdb-r9tzcdd0.cd.tencentcdb.com',
                               port=10125,
                               user='root',
                               passwd="tenderkun123",
                               db='towhere')
        jsonData = r.json()
        date = time.localtime(time.time())
        sqldate = time.strftime("%Y-%m-%d %X", date)
        pop_data = jsonData
        items = pop_data['data']['site']["subs"][0]['items']
        ties = pop_data['data']['site']["subs"][1]['items']

        rank = 1
        for item in items:
            print(item)
            cur = conn.cursor()
            sql = "insert into rank_baidu(iid,title,add_date,get_date,rank,more) values('%d','%s','%d','%s','%d'," \
                  "'%s') "
            data = (item['iid'], item['title'], item['add_date'], sqldate, rank, item['more'])
            # print(sql % data)
            cur.execute(sql % data)
            rank += 1
            conn.commit()
        rank = 1
        for tie in ties:
            print(tie)
            cur = conn.cursor()
            sql = "insert into tieba(iid,title,add_date,get_date,rank,more) values('%d','%s','%d','%s','%d'," \
                  "'%s') "
            data = (tie['iid'], tie['title'], tie['add_date'], sqldate, rank, tie['more'])
            # print(sql % data)
            cur.execute(sql % data)
            rank += 1
            conn.commit()


if __name__ == '__main__':
    print('get once')
    getBaidu()
