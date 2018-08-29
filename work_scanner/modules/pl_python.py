from modules.site import Site
import re


class PlPython(Site):
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
        self.find_offers()

        while self.page < self.max_pages:
            self.next_page()
            self.find_offers()

    def find_offers(self):
        html = str(self.get_html()).lower()
        for match in re.findall('a href=\"(https://pl\.python\.org/forum/index\.php\?topic=[0-9.]+)\"', html):
            self.url = match
            self.search_for_keywords()

    def search_for_keywords(self):
        html = str(self.get_html()).lower()
        if any(keyword in html for keyword in self.keywords):
            date = re.search('&#171; {2}: ([0-9:/ ]+) &#187;', html)
            print(date.group(1), self.url)

