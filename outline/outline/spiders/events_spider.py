import scrapy


class EventsSpider(scrapy.Spider):
    name = "events"

    def start_requests(self):
        start_urls = [
            'http://www.outlineonline.co.uk/events',
        ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'events-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)