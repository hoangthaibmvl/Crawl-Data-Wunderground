# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetWeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    Time = scrapy.Field()
    Temperature = scrapy.Field()
    Dew_Point = scrapy.Field()
    Humidity = scrapy.Field()
    Wind = scrapy.Field()
    Wind_Speed = scrapy.Field()
    Wind_Gust = scrapy.Field()
    Pressure = scrapy.Field()
    Precip = scrapy.Field()
    Condition = scrapy.Field()