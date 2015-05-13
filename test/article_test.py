import unittest
import sys
from article import Article

sys.path.append('../src')

class TestArticle(unittest.TestCase):

    def test_date(self):
        self.assertEqual(Article.parse_date(""), None)
        self.assertEqual(str(Article.parse_date("13:29 08.09.2008")), "2008-09-08 13:29:00")

suite = unittest.TestLoader().loadTestsFromTestCase(TestArticle)
unittest.TextTestRunner(verbosity=2).run(suite)