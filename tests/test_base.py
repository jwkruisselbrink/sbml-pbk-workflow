import unittest
import pathlib as pl

__test_outputs_path__ = './tests/__testoutputs__'

class TestBase(unittest.TestCase):

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

if __name__ == '__main__':
    unittest.main()
