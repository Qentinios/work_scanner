from modules.site import Site
import re


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
        for match in re.findall('a href=\"(https://pl\.python\.org/forum/index\.php\?topic=[0-9.]+)\"', html):
            self.url = match

            html2 = self.get_html_lower()
            self.search_for_keywords(html2)

    def search_for_keywords(self, html2):
        if any(keyword in html2 for keyword in self.keywords):
            date = re.search('&#171; {2}: ([0-9:/ ]+) &#187;', html2)
            print(date.group(1), self.url)

