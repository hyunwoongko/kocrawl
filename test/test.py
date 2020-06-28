"""
@auther Hyunwoong
@since 6/29/2020
@see https://github.com/gusdnd852
"""
from kocrawl.weather import WeatherCrawler

c = WeatherCrawler()
print(c.request_debug(location='런던', date='1901년 3월 2일'))
