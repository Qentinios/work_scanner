from modules.base.site import Site
import re
from ast import literal_eval


class PlPython(Site):
    page = 1
    url = 'https://pl.python.org/forum/index.php?board=9.0'

    def __init__(self, max_pages, keywords=None):
        if keywords is None:
            keywords = []
        self.max_pages = max_pages
        self.keywords = keywords

    def next_page(self):
        link_end = 20 * self.page
        self.url = 'https://pl.python.org/forum/index.php?board=9.' + str(link_end)
        self.page += 1

    def scan(self):
        html = self.get_html_lower()
        self.find_offers(html)

        while self.page < self.max_pages:
            self.next_page()

            html = self.get_html_lower()
            self.find_offers(html)

    def find_offers(self, html):
        for match in re.finditer('a href=\"(?P<link>https://pl\.python\.org/forum/index\.php\?topic=[?P<link>0-9.]+)\">(?P<title>.*?)</.*?smalltext\">(?P<date>.*?)<', html, flags=re.S):
            self.url = match.group('link')
            date = match.group('date').replace('\\n', "").replace('\\t', "")

            title_encoded = match.group('title')
            title = literal_eval("b'{}'".format(title_encoded)).decode('utf-8')

            html2 = self.get_html_lower()
            self.search_for_keywords(html2, title, date)

    def search_for_keywords(self, html2, title, date):
        if any(keyword in html2 for keyword in self.keywords):
            print(date, title, self.url)

