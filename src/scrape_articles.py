from article import Article, ArticleEncoder
import json

articles = []

for article_id in range(21, 24):
    a = Article.get_article(article_id)
    print("{:0}: ".format(article_id), end="")
    print(a.title if a else "---")

    if a:
        articles.append(a)

# Save JSON to file
with open('../data/data.txt', 'w') as outfile:
    print(outfile)
    json.dump(articles, outfile, cls=ArticleEncoder)


dump = json.dumps(articles, cls=ArticleEncoder)
articles2 = json.JSONDecoder(object_hook=Article.from_json).decode(dump)
