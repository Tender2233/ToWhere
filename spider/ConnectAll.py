import time

import Sguoke, Stoutiao, Syc, Sweibo, S36kr, Sbilibili, Sqdaily, S163, Spengpai, Spearvideo, Szhihu, Sbaidu


def keep():
    while True:
        S163.get163()
        Sbaidu.getBaidu()
        Sweibo.getWeibo()
        Szhihu.getZhihu()
        Sqdaily.getQdaily()
        S36kr.get36kr()
        Sbilibili.getBilibili()
        Spearvideo.getPearVideo()
        Spengpai.getPengpai()
        Stoutiao.getToutiao()
        Syc.getYc()
        Sguoke.getGuoker()
        print('单次获取完成，等待5min')
        time.sleep(300)


def once():
    S163.get163()
    Sbaidu.getBaidu()
    Sweibo.getWeibo()
    Szhihu.getZhihu()
    Sqdaily.getQdaily()
    S36kr.get36kr()
    Sbilibili.getBilibili()
    Spearvideo.getPearVideo()
    Spengpai.getPengpai()
    Stoutiao.getToutiao()
    Syc.getYc()
    Sguoke.getGuoker()


if __name__ == '__main__':
    # keep()
    once()
