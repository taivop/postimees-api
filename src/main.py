from article import Article
from lxml import html
import requests

url1 = "http://wap.postimees.ee/index.php?wid=50000"
url2 = "http://wap.postimees.ee/index.php?wid=3150000"
url3 = "http://wap.postimees.ee/index.php?wid=3187079"
url4 = "http://wap.postimees.ee/index.php?wid=3189279"

page = requests.get(url1)

tree = html.fromstring(page.content)

article_title = tree.xpath('//card/p/b/text()')
article_date = tree.xpath('//card/p[1]/text()')
article_text = tree.xpath('//card/p[2]/text()')

a = Article(article_title[0], article_date[0], article_text[0])
print(a)
