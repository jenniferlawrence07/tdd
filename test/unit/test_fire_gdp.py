import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../src")
    )
)

import fire_gdp  # noqa: E402


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        header = ["Country", "1990", "1991"]
        result = fire_gdp.get_column_index(header, "1990")
        self.assertEqual(result, 1)

    def test_name_absent(self):
        header = ["Country", "1990", "1991"]
        result = fire_gdp.get_column_index(header, "2000")
        self.assertIsNone(result)

    def test_empty_header(self):
        header = []
        result = fire_gdp.get_column_index(header, "1990")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
