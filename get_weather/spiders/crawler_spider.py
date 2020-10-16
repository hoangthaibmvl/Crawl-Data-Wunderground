from scrapy import Spider
from scrapy.selector import Selector
from get_weather.items import GetWeatherItem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = [
        "www.wunderground.com"]
    # # start_urls = [
    # #     "https://www.wunderground.com/history/daily/vn/qu%E1%BA%ADn-t%C3%A2n-b%C3%ACnh/VVTS/date/2020-10-%d" ,
    # # ]

    # start_urls = url

    def __init__(self, url, *args, **kwargs):
        self.driver = webdriver.Firefox()
        super(CrawlerSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'{url}']

    def parse(self, response):
        self.driver.implicitly_wait(60)
        self.driver.get(response.url)
        self.driver.find_elements(
            By.XPATH, '//table[@class="mat-table cdk-table mat-sort ng-star-inserted"]')
        html = self.driver.page_source
        body = Selector(text=html)
        table = body.xpath(
            '//*[@class="observation-table ng-star-inserted"]/table[@class="mat-table cdk-table mat-sort ng-star-inserted"]/tbody/tr')
        for row in table:
            item = GetWeatherItem()
            # Pre-check
            Time = row.xpath('td/span/text()')[0].extract()
            Temperature = row.xpath(
                'td/lib-display-unit/span/span/text()')[0].extract()
            Dew_Point = row.xpath(
                'td/lib-display-unit/span/span/text()')[1].extract()
            Humidity = row.xpath(
                'td/lib-display-unit/span/span/text()')[2].extract()
            check = row.xpath('td/span/text()').extract()
            if (len(check) == 2):
                Wind = ""
                Condition = row.xpath('td/span/text()')[1].extract()
            else:
                Wind = row.xpath('td/span/text()')[1].extract()
                Condition = row.xpath('td/span/text()')[2].extract()
            Wind_Speed = row.xpath(
                'td/lib-display-unit/span/span/text()')[3].extract()
            Wind_Gust = row.xpath(
                'td/lib-display-unit/span/span/text()')[4].extract()
            Pressure = row.xpath(
                'td/lib-display-unit/span/span/text()')[5].extract()
            Precip = row.xpath(
                'td/lib-display-unit/span/span/text()')[6].extract()
            if (Time == ''):
                Time = "NoData"
            if (Temperature == ''):
                Temperature = "NoData"
            if (Dew_Point == ''):
                Dew_Point = "NoData"
            if (Humidity == ''):
                Humidity = "NoData"
            if (Wind == ''):
                Wind = "NoData"
            if (Wind_Speed == ''):
                Wind_Speed = "NoData"
            if (Wind_Gust == ''):
                Wind_Gust = "NoData"
            if (Pressure == ''):
                Pressure = "NoData"
            if (Precip == ''):
                Precip = "NoData"
            if (Condition == ''):
                Condition = "NoData"
            item['Time'] = Time
            item['Temperature'] = Temperature
            item['Dew_Point'] = Dew_Point
            item['Humidity'] = Humidity
            item['Wind'] = Wind
            item['Wind_Speed'] = Wind_Speed
            item['Wind_Gust'] = Wind_Gust
            item['Pressure'] = Pressure
            item['Precip'] = Precip
            item['Condition'] = Condition
            yield item
        self.driver.close()
