import re
import requests

class Spider(object):

    def __init__(self):
        self.headers = {}
        self.content = ''
        self.result = ''

    def get_headers(self):
        header_string = '''
            Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
            Accept-Encoding:gzip, deflate, br
            Accept-Language:zh-CN,zh;q=0.9,en;q=0.8
            Connection:keep-alive
            Host:baike.baidu.com
            Upgrade-Insecure-Requests:1
            User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36
            '''
        header = header_string.split('\n')
        for elem in header:
            if len(elem.strip()) == 0:
                pass
            else:
                self.headers[elem.split(':')[0].strip()] = elem.split(':')[1].strip()


    def download(self, query):
        self.get_headers()
        response = requests.get('https://baike.baidu.com/item/' + query, headers = self.headers)
        self.content = response.content.decode('utf-8')

    def parse(self):
        reg_content = '<div class="lemma-summary" label-module="lemmaSummary">[\s\S]+?</div>'
        reg_result = re.findall(reg_content, self.content)[0]
        self.result = re.sub('<.+?>', '', reg_result).strip()

    def start(self, query):
        self.download(query)
        self.parse()
        print(self.result.replace('\n',''))
        return self.result

if __name__ == '__main__':
    spider = Spider()
    spider.start('写轮眼')