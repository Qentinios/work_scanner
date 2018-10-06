import unittest

from modules.linkedin import LinkedIn
from modules.pl_python import PlPython
from modules.pracuj_pl import PracujPl


class ModulesTest(unittest.TestCase):
    pl_python = PlPython(max_pages=3, keywords=[])
    linked_in = LinkedIn(keywords=[])
    pracuj_pl = PracujPl(max_pages=10, keywords=[])

    def test_pl_python_download(self):
        self.assertTrue(len(self.pl_python.get_html_lower()) > 1000)

    def test_pl_python_next_page(self):
        for i in range(5):
            self.pl_python.next_page()

        self.assertEqual('https://pl.python.org/forum/index.php?board=9.100', self.pl_python.url)

    def test_linkedin_token(self):
        self.assertTrue(hasattr(self.linked_in, 'application'))


if __name__ == '__main__':
    unittest.main()
