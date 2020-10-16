import subprocess
import sys
import getopt

dates = ["2000-01-20","2000-12-19","2000-09-29","2000-05-14"]
year = 2000


url = "file:///home/hoangthai/get_weather/html/"
for date in dates:
    process = subprocess.Popen(['scrapy', 'runspider', '/home/hoangthai/get_weather/get_weather/spiders/crawler_spider.py',
                                '-a', 'url='+url+date+'.html', '-o', './data/' + str(year) + '/'+date+'.csv'])
    process.wait()
