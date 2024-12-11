import unittest
import pathlib as pl
import src.validate_sbml
from tests.test_base import TestBase
from unittest.mock import patch

class TestValidateSbml(TestBase):

    @patch('sys.argv', ['ant2sbml.py', './tests/models/simple.annotated.sbml', '-l', './tests/output/simple.annotated.validation.log'])
    def test_simple_log_file(self):
        src.validate_sbml.main()
        path = pl.Path('./tests/output/simple.annotated.validation.log')
        self.assertIsFile(path)

    @patch('sys.argv', ['ant2sbml.py', './tests/models/simple.annotated.sbml'])
    def test_simple_log_console(self):
        src.validate_sbml.main()

if __name__ == '__main__':
    unittest.main()
