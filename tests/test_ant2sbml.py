import unittest
import pathlib as pl
import src.ant2sbml
from tests.test_base import TestBase
from unittest.mock import patch

class TestAnt2Sbml(TestBase):

    @patch('sys.argv', ['ant2sbml.py', './tests/models/simple.ant', './tests/output/simple.sbml'])
    def test_simple(self):
        src.ant2sbml.main()
        path = pl.Path('./tests/output/simple.sbml')
        self.assertIsFile(path)

if __name__ == '__main__':
    unittest.main()
