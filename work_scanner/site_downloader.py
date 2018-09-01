import urllib.request


class Downloader:

    def __init__(self, url):
        self.url = url

    def download(self, headers=None):
        if headers is None:
            req = urllib.request.Request(self.url)
        else:
            req = urllib.request.Request(self.url, headers=headers)
        response = urllib.request.urlopen(req)
        return response.read()
