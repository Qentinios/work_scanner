import re
import time

from modules.base.web_browser import WebBrowser


class PracujPl(WebBrowser):
    page = 1
    url = 'https://www.pracuj.pl/praca/python;kw'

    def __init__(self, max_pages, keywords=None):
        super().__init__(self.url)
        if keywords is None:
            keywords = []
        self.max_pages = max_pages
        self.keywords = keywords

    def next_page(self):
        self.url = 'https://www.pracuj.pl/praca/python;kw?pn=' + str(self.page)
        self.page += 1

    def scan(self):
        self.find_offers()

        while self.page < self.max_pages:
            self.next_page()

            self.browser.get(self.url)
            self.find_offers()

    def find_offers(self):
        offer_elements = self.browser.find_elements_by_css_selector('li[data-offer-item]')

        offers = []
        for offer_element in offer_elements:
            title = offer_element.find_element_by_class_name('o-list_item_link_name')

            if "python" in title.text.lower():
                link = offer_element.find_element_by_css_selector('a[data-gtm-offer]')
                date = offer_element.find_element_by_class_name('o-list_item_desc_date')

                offers.append(
                    {
                        "url": link.get_attribute('href'),
                        "title": title.text,
                        "date": date.text
                    }
                )

        for offer in offers:
            self.check_offer(offer)

    def check_offer(self, offer):
        page = self.get_url(offer['url'])
        time.sleep(1)

        if self.search_for_keywords(page.page_source):
                print(offer["date"], offer['title'], offer['url'])

    def search_for_keywords(self, html2):
        if any(keyword in html2 for keyword in self.keywords):
            return True
        return False
