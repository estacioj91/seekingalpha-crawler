from scrapy import Spider
from scrapy.selector import Selector


from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["seekingalpha.com"]
    start_urls = [
        "https://seekingalpha.com/market-news",
    ]

    # //*[@id="latest-news-list"]/li/a[@class="item"]/text()
    all_urls = []

    def parse(self, response):
        questions = Selector(response).xpath('//li[@class="item"]')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'h4/a/text()').extract()[0]
            item['url'] = "https://seekingalpha.com" + question.xpath(
                'h4/a/@href').extract()[0]
            self.all_urls.append(item['url'])
        print(self.all_urls)
        for url in self.all_urls:
            # get content for url to be parsed. USE CALLBACK
        yield scrapy.Request(url, callback=self.parse_url)

    def parse_url(self, response)
    # h4/a/text()
