import requests

def baidu():
    r = requests.get('https://www.anyknew.com/api/v1/sites/baidu')

    print(r.status_code)
    print(r.headers)
    print(r.json())

if __name__ == '__main__' :
    print('test begin')
    baidu()