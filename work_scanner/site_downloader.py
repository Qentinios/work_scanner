import urllib.request


class Downloader:

    def __init__(self, url):
        self.url = url

    def download(self):
        req = urllib.request.Request(self.url)
        response = urllib.request.urlopen(req)
        return response.read()
