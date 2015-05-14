from datetime import datetime
from lxml import html
from json import JSONEncoder
import requests

class Article:
    """A single article object."""

    def __init__(self, article_id, title, date, text):
        self.article_id = article_id
        self.title = title
        self.date_string = date
        self.date = self.parse_date(self.date_string)
        self.text = text

    def __str__(self):
        screen_width = 80
        chunks = [self.text[i:i+screen_width] for i in range(0, len(self.text), screen_width)]
        a = ["", self.title, str(self.date), ""] + chunks
        return "\n> ".join(a)

    def to_csv(self):
        """Produce a CSV line from the article"""
        a = [str(self.article_id), str(self.date), '"' + self.title + '"', '"' + self.text.replace("\n", " ") + '"']
        return ";".join(a)

    @staticmethod
    def parse_date(date_string):
        """Parse date string from article text into datetime object."""

        l = len(date_string)
        current = datetime.now()

        # If empty
        if l == 0:
            return None
        # If only time
        elif l <= 5:
            d_format = "%H:%M"
            dt = datetime.strptime(date_string, d_format)
            dt = dt.replace(day=current.day, month=current.month, year=current.year)
        # If datetime without year
        elif l <= 11:
            d_format = "%H:%M %d.%m"
            dt = datetime.strptime(date_string, d_format)
            dt = dt.replace(year=current.year)
        # If the whole shebang
        else:
            d_format = "%H:%M %d.%m.%Y"
            dt = datetime.strptime(date_string, d_format)
        return dt

    @staticmethod
    def get_article(article_id):
        """Download article with the given ID and return Article object built from it."""

        # Build request URL
        url = "http://wap.postimees.ee/index.php?wid=" + str(article_id)

        # Pull page and parse HTML tree
        page = requests.get(url)
        tree = html.fromstring(page.content)

        # Extract data from the fields
        title = tree.xpath('//card/p/b/text()')
        date = tree.xpath('//card/p[1]/text()')
        text = tree.xpath('//card/p[2]/text()')

        # Build Article object
        if title and date and text:
            return Article(article_id, title[0], date[0], "\n".join(text))
        else:
            return None

    @staticmethod
    def from_json(json_object):
        return Article(int(json_object['article_id']),
                       json_object['title'],
                       json_object['date'],
                       json_object['text'])



class ArticleEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            obj = str(o)
        elif isinstance(o, Article):
            obj = o.__dict__
        else:
            obj = JSONEncoder.default(self, o)

        return obj