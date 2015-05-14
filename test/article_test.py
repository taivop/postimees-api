import unittest
import sys
from article import Article, ArticleEncoder

sys.path.append('../src')

class TestArticle(unittest.TestCase):

    def test_date(self):
        self.assertEqual(Article.parse_date(""), None)
        self.assertEqual(str(Article.parse_date("13:29 08.09.2008")), "2008-09-08 13:29:00")

    def test_download(self):
        self.assertEqual(Article.get_article(318700).title, "Priit Rätsep kihutas Rahvuste krossil")
        self.assertEqual(Article.get_article(31870), None)
        self.assertEqual(str(Article.get_article(3).date), "2007-07-16 16:42:00")

    def test_encode(self):
        article = Article(0, "Testartikkel", "13:29 08.09.2008", "Testartikli tekst.")
        self.assertEqual(ArticleEncoder().encode(article), "taivo")

suite = unittest.TestLoader().loadTestsFromTestCase(TestArticle)
unittest.TextTestRunner(verbosity=2).run(suite)