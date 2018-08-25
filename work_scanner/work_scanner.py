from site_downloader import Downloader

downloader = Downloader('https://pl.python.org/forum/index.php?board=9.0')
content = downloader.download()
print(content)

