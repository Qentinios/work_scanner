from modules.goldenline import Goldenline
from modules.linkedin import LinkedIn
from modules.pl_python import PlPython
from modules.pracuj_pl import PracujPl

print('### linkedin.com/ ###')
linked_in = LinkedIn(keywords=['remote', 'zdalna', 'zdalnie', 'home office'])
if hasattr(linked_in, 'application'):
    linked_in.scan()

print('### pl.python.org/ ###')
pl_python = PlPython(max_pages=3, keywords=['remote', 'zdalna', 'zdalnie', 'home office'])
pl_python.scan()
del pl_python

print('### pracuj.pl/ ###')
pracuj_pl = PracujPl(max_pages=20, keywords=['remote', 'zdalna', 'zdalnie', 'home office'])
pracuj_pl.scan()
del pracuj_pl

print('### goldenline.pl/ ###')
goldenline = Goldenline(max_pages=2, keywords=['remote', 'zdalna', 'zdalnie', 'home office'])
goldenline.scan()
del goldenline

