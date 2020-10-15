import subprocess

dates = []
for x in range(1, 30):
    dates.append("2020-09-%d" % x)


url = "https://www.wunderground.com/history/daily/vn/qu%E1%BA%ADn-t%C3%A2n-b%C3%ACnh/VVTS/date/"
for date in dates:
    process = subprocess.Popen(['scrapy', 'runspider', '/home/hoangthai/get_weather/get_weather/spiders/crawler_spider.py',
                                '-a', 'url='+url+date, '-o', './data/'+date+'.csv'])
    process.wait()
