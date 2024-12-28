import requests
from lxml import etree

class Douban():
    def __init__(self):
        self.url = 'https://book.douban.com/top250'
        self.header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        }

    # 向列表页发送请求
    def get_data(self, url):
        r = requests.get(url, headers=self.header)
        r.encoding = 'utf-8'
        return r.text

    def parse_data(self, data):
        xml = etree.HTML(data)
        hrefs = xml.xpath(
            '//td[@valign="top"]/a/img/@src|//tr[@class="item"]/td/div/a/@href|//tr[@class="item"]/td/div/a/@title|//tr[@class="item"]/td/p/text()')
        # print(hrefs)
        return hrefs

    def main(self):
        html_data = self.get_data(self.url)
        hrefs = self.parse_data(html_data)
        for href in hrefs:
            print(href)


if __name__ == '__main__':
    s = Douban()
    s.main()
