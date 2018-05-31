from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

resp = urlopen(request)

print(resp)

html = resp.read().decode('cp949')

bs = BeautifulSoup(html,'html.parser')


tags = bs.findAll('div', attrs={'class':'tit3'})
#print(tags)

for index,tag in enumerate(tags):
    print(index,tag.a.text, tag.a['href'], sep=":")


#print(bs.prettify())