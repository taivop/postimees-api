
class Article:
    """A single article object."""

    def __init__(self, title, date, text):
        self.title = title[0]
        self.date = date[0]
        self.text = text[0]

    def __str__(self):
        screen_width = 80
        chunks = [self.text[i:i+screen_width] for i in range(0, len(self.text), screen_width)]
        a = ["", self.title, self.date, ""] + chunks
        return "\n> ".join(a)