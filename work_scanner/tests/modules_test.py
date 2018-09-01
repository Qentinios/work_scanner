import unittest
from modules.pl_python import PlPython


class ModulesTest(unittest.TestCase):
    pl_python = PlPython(max_pages=3, keywords=[])

    def test_pl_python_download(self):
        self.assertTrue(len(self.pl_python.get_html_lower()) > 1000)

    def test_pl_python_next_page(self):
        for i in range(5):
            self.pl_python.next_page()

        self.assertEqual(self.pl_python.url, 'https://pl.python.org/forum/index.php?board=9.100')


if __name__ == '__main__':
    unittest.main()
