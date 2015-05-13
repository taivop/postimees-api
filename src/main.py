from lxml import html
import requests
from article import Article

url1 = "http://wap.postimees.ee/index.php?wid=50000"
url2 = "http://wap.postimees.ee/index.php?wid=3150000"
url3 = "http://wap.postimees.ee/index.php?wid=3189279"

page = requests.get(url1)

tree = html.fromstring(page.content)

article_title = tree.xpath('//card/p/b/text()')
article_date = tree.xpath('//card/p[1]/text()')
article_text = tree.xpath('//card/p[2]/text()')

a = Article(article_title, article_date, article_text)
print(a)
