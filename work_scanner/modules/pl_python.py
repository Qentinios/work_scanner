from modules.site import Site
import re


class PlPython(Site):
    url = 'https://pl.python.org/forum/index.php?board=9.0'

    def __init__(self, maxpages):
        self.max_pages = maxpages

    def next_page(self):
        link_end = 20 * self.page
        self.url = 'https://pl.python.org/forum/index.php?board=9.' + str(link_end)
        self.page += 1

    def scan(self):
        self.find_offers()

        while self.page < self.max_pages:
            self.next_page()
            self.find_offers()

    def search_for_keywords(self):
        pass

    def find_offers(self):
        html = self.get_html()
        for match in re.findall('a href=\"(https://pl\.python\.org/forum/index\.php\?topic=[0-9.]+)\"', str(html)):
            print(match)


