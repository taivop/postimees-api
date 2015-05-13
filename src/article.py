from datetime import datetime, timedelta

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
        l = len(date_string)
        current = datetime.now()

        # If empty
        if l == 0:
            return None
        # If only time
        elif l <= 5:
            format = "%H:%M"
            dt = datetime.strptime(date_string, format)
            dt = dt.replace(day=current.day, month=current.month, year=current.year)
        # If datetime without year
        elif l <= 11:
            format = "%H:%M %d.%m"
            dt = datetime.strptime(date_string, format)
            dt = dt.replace(year=current.year)
        # If the whole shebang
        else:
            format = "%H:%M %d.%m.%Y"
            dt = datetime.strptime(date_string, format)
        return dt


