from site_downloader import Downloader


class Site:
    page = 1
    url = None

    def get_html(self):
        if self.url is None:
            return None

        downloader = Downloader(self.url)
        content = downloader.download()
        return content
