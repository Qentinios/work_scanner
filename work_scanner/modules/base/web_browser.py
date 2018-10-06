import time

from selenium import webdriver


class WebBrowser:
    url = ""
    browser = None
    driver = webdriver

    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        time.sleep(2)

    def get_page(self, page):
        self.url = self.url + page
        self.browser.get(self.url)

        return self.browser

    def get_url(self, url):
        self.url = url
        self.browser.get(self.url)

        return self.browser

