from scripts.site_downloader import Downloader


class Site:
    url = None

    def get_html(self):
        if self.url is None:
            return None

        downloader = Downloader(self.url)
        content = downloader.download()
        return content

    def get_html_mock_browser(self):
        if self.url is None:
            return None

        downloader = Downloader(self.url)

        hdr = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3218.0 Safari/537.36',
            'Connection': 'keep-alive'}

        content = downloader.download(hdr)
        return content

    def get_html_lower(self):
        return str(self.get_html()).lower()

