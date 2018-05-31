# 一开始只是网页
import requests
r=requests.get('https://book.douban.com/subject/1084336/comments/')
# 看看是否获取承购
r.status_code
print(r.text)
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
r=requests.get('https://book.douban.com/subject/1084336/comments/',headers=headers)
r
# 核心的：爬取豆瓣评论文本
import requests
from bs4 import BeautifulSoup
r=requests.get('https://book.douban.com/subject/1084336/comments/')
soup=BeautifulSoup(r.text,'lxml')
r.text
pattern=soup.find_all('p',{'class':'comment-content'})
print(pattern)
# 只保留文本！
for item in pattern:
    print(item.text)