from datetime import datetime
from lxml import html
import requests

class Article:
    """A single article object."""

    def __init__(self, title, date, text):
        self.title = title
        self.date_string = date
        self.date = self.parse_date(self.date_string)
        self.text = text

    def __str__(self):
        screen_width = 80
        chunks = [self.text[i:i+screen_width] for i in range(0, len(self.text), screen_width)]
        a = ["", self.title, str(self.date), ""] + chunks
        return "\n> ".join(a)


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
    def get_article(id):
        """Download article with the given ID and return Article object built from it."""

        # Build request URL
        url = "http://wap.postimees.ee/index.php?wid=" + str(id)

        # Pull page and parse HTML tree
        page = requests.get(url)
        tree = html.fromstring(page.content)

        # Extract data from the fields
        title = tree.xpath('//card/p/b/text()')
        date = tree.xpath('//card/p[1]/text()')
        text = tree.xpath('//card/p[2]/text()')

        # Build Article object
        if title and date and text:
            return Article(title[0], date[0], text[0])
        else:
            return None


