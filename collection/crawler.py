from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import sys
#유알엘 , 엔코딩 방식, html 가져왔을 때 처리하는 방식

#def proc(html):
 #   return html

#def store(src):
#    return src

#def

def crawling(
        url='',
        encoding='utf-8',
        proc=lambda html:html,
        store=lambda data:data,
        err = lambda e:print('%s: %s'%(e, datetime.now()),file=sys.stderr)):
    try:
        request = Request(url)

        resp = urlopen(request)

        try:
            receive = resp.read()

            result = receive.decode(encoding)
        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')

        print('%s : success for request [%s]' % (datetime.now(), url))
        return store(proc(result))
    except  Exception as e:
        err(e)