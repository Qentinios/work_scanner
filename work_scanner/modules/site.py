from site_downloader import Downloader


class Site:
    page = 1
    url = ''

    def get_html(self):
        downloader = Downloader(self.url)
        content = downloader.download()
        return content
