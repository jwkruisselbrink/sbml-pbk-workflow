import unittest
import pathlib as pl
import src.annotate_sbml
from tests.test_base import TestBase
from unittest.mock import patch

class TestAnnotateSbml(TestBase):

    @patch('sys.argv', ['ant2sbml.py', './tests/models/simple.sbml', './tests/models/simple.annotations.csv', './tests/output/simple.annotated.sbml', '-f'])
    def test_simple(self):
        src.annotate_sbml.main()
        path = pl.Path('./tests/output/simple.annotated.sbml')
        self.assertIsFile(path)

if __name__ == '__main__':
    unittest.main()
