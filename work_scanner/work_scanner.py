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

print('### pracuj.pl/ ###')
pracuj_pl = PracujPl(max_pages=10, keywords=['remote', 'zdalna', 'zdalnie', 'home office'])
pracuj_pl.scan()

