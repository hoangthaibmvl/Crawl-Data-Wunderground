import subprocess
import sys
import getopt
from multiprocessing import Pool


year = int(sys.argv[1])
dates = []
for x in range(1, 13):
    for y in range(1, 32):
        dates.append("%d-%d-%d" % (year, x, y))


url = "https://www.wunderground.com/history/daily/vn/qu%E1%BA%ADn-t%C3%A2n-b%C3%ACnh/VVTS/date/"
for date in dates:
    process = subprocess.Popen(['scrapy', 'runspider', '/home/hoangthai/get_weather/get_weather/spiders/crawler_spider.py',
                                '-a', 'url='+url+date, '-o', './data/' + str(year) + '/' + date+'.csv'])
    process.wait()
