import random
import time

from selenium.common.exceptions import NoSuchElementException
from modules.base.web_browser import WebBrowser


class Goldenline(WebBrowser):
    page = 1
    url = 'https://www.goldenline.pl/praca/szukaj?query=python'

    def __init__(self, max_pages, keywords=None):
        super().__init__(self.url)
        if keywords is None:
            keywords = []
        self.max_pages = max_pages
        self.keywords = keywords

    def next_page(self):
        self.page += 1
        self.url = 'https://www.goldenline.pl/praca/szukaj' + str(self.page) + '?query=python'

    def scan(self):
        self.find_offers()

        while self.page < self.max_pages:
            self.next_page()

            self.browser.get(self.url)
            self.find_offers()

    def find_offers(self):
        try:
            self.browser.find_element_by_class_name('agree').click()
            time.sleep(1)
        except NoSuchElementException:
            pass

        offer_elements = self.browser.find_elements_by_css_selector('a[typeof="JobPosting"]')

        offers = []
        for offer_element in offer_elements:
            title = offer_element.find_element_by_class_name('position')
            date = offer_element.find_element_by_css_selector('span[property="datePosted"]')

            offers.append(
                {
                    "url": offer_element.get_attribute('href'),
                    "title": title.text,
                    "date": date.get_attribute("innerHTML")
                }
            )

        for offer in offers:
            self.check_offer(offer)

    def check_offer(self, offer):
        page = self.get_url(offer['url'])

        try:
            html = page.find_element_by_xpath('//div[@id="offer_header"]/following::div[1]').get_attribute('innerHTML')
        except NoSuchElementException:
            input("CAPTCHA: You need to confirm manually on your browser (go to https://www.goldenline.pl/ ) and "
                  "enter any key")

            self.get_url('https://www.goldenline.pl/')
            time.sleep(3)
            page = self.get_url(offer['url'])
            html = page.find_element_by_xpath('//div[@id="offer_header"]/following::div[1]').get_attribute('innerHTML')

        if self.search_for_keywords(html):
                print(offer["date"], offer['title'], offer['url'])

        time.sleep(1)

    def search_for_keywords(self, html):
        if any(keyword in html for keyword in self.keywords):
            return True
        return False

