import unittest
import pathlib as pl
import src.validate_sbml
from tests.test_base import TestBase
from unittest.mock import patch

class TestValidateSbml(TestBase):

    @patch('sys.argv', ['ant2sbml.py', './tests/models/simple.annotated.sbml', './tests/output/simple.annotated.validation.log'])
    def test_simple(self):
        src.validate_sbml.main()
        path = pl.Path('./tests/output/simple.annotated.validation.log')
        self.assertIsFile(path)

if __name__ == '__main__':
    unittest.main()
