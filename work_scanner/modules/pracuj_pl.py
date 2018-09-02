from modules.site import Site
import re


class PracujPl(Site):
    page = 1
    url = 'https://www.pracuj.pl/praca/python;kw'

    def __init__(self, max_pages, keywords=None):
        if keywords is None:
            keywords = []
        self.max_pages = max_pages
        self.keywords = keywords

    def next_page(self):
        self.url = 'https://www.pracuj.pl/praca/python;kw?pn=' + str(self.page)
        self.page += 1

    def scan(self):
        html = self.get_html_lower()
        self.find_offers(html)

        while self.page < self.max_pages:
            self.next_page()

            html = self.get_html_lower()
            self.find_offers(html)

    def find_offers(self, html):
        pattern = 'data-test=\"offertitlecnt\" .*?<a href=\"(.*?)\".*?title=\".*?\">(.*?)<.*?dateposted\">(.*?)<'
        for match in re.findall(pattern, html, flags=re.M):
            link = 'https://www.pracuj.pl' + match[0]
            title = match[1]
            date = match[2]
            self.url = link

            html2 = self.get_html_lower()
            if self.search_for_keywords(html2):
                print(link, title, date)

    def search_for_keywords(self, html2):
        if any(keyword in html2 for keyword in self.keywords):
            return True
        return False

