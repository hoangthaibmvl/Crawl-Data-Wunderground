import subprocess
import sys
import getopt
from multiprocessing import Pool
import multiprocessing
import time


def process(date, year):
    url = "https://www.wunderground.com/history/daily/vn/qu%E1%BA%ADn-t%C3%A2n-b%C3%ACnh/VVTS/date/"
    process = subprocess.Popen(['scrapy', 'runspider', '/home/hoangthai/get_weather/get_weather/spiders/crawler_spider.py',
                                '-a', 'url='+url+date, '-o', './data/' + str(year) + '/' + date+'.csv'])


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    year = int(sys.argv[1])
    dates = []
    max_apply_size = 3
    for x in range(1, 2):
        for y in range(1, 31):
            dates.append("%d-%d-%d" % (year, x, y))
    for date in dates:
        pool.apply_async(process, args=(date, year,))
        while pool._taskqueue.qsize() > max_apply_size:
            time.sleep(3)
    pool.close()
    pool.join()
